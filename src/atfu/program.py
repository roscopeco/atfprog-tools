import io
import re
import os.path
import atfu.erase
import atfu.verify
from atfu.output import Output, cbYellow, cReset
from atfu.little_board.jtag_programmer import JtagProgrammer
from atfu.converter.jed2svf import jed2svf
from atfu.converter.svf2xsvf import svf2xsvf
from atfu.device_id import check_chip_id


def handler(args):
    output = Output(args)

    prog = JtagProgrammer(
        "PROGRAM", args.programmer, output.verbosity(), no_success=False
    )

    if args.erase or args.force:
        erase_result = atfu.erase.perform_erase(
            args, no_success=False, reuse_serial=prog.serial()
        )
        if erase_result != 0:
            exit(erase_result)

    if not check_chip_id(args, output, reuse_serial=prog.serial()):
        output.error(args.device, "not found, please check device type and connection")
        return 1

    will_verify = not args.noverify and True not in (
        bool(re.search(r"[Xx]?[Ss][Vv][Ff]$", fn.name)) for fn in args.filename
    )

    xsvf_files = _process_input_files(args.device, args.filename, output)

    if prog.upload_all_files(xsvf_files):
        if not args.noverify:
            if not will_verify:
                output.output(
                    1,
                    f"{cbYellow}Warning{cReset} Verification specified, but skipped due to SVF/XSVF input file",
                )
            else:
                verify_result = atfu.verify.perform_verify(
                    args, reuse_serial=prog.serial()
                )
                if verify_result != 0:
                    exit(verify_result)

        exit(0)
    else:
        exit(1)


def _process_input_files(
    device: str, files: list[io.BufferedReader], output: Output
) -> list[io.BufferedReader]:
    return [_process_input_file(device, result_file, output) for result_file in files]


def _process_input_file(device: str, file: io.BufferedReader, output: Output):
    if re.search(r"[Jj][Ee][Dd]$", file.name):
        # Never erase or verify here, we do those separately for better error reporting...
        return _process_input_svf(output, _process_input_jed(output, device, file))
    elif re.search(r"[^Xx][Ss][Vv][Ff]$", file.name):
        return _process_input_svf(output, file)
    elif re.search(r"[Xx][Ss][Vv][Ff]$", file.name):
        return file
    else:
        output.error(
            "Failure", f"File type for {os.path.basename(file.name)}; Cannot continue"
        )
        exit(80)


def _process_input_jed(
    output: Output, device: str, file: io.BufferedReader
) -> io.BufferedReader:
    return jed2svf(
        device=device,
        infile=file,
        output=output,
        erase=False,
        program=True,
        verify=False,
    )


def _process_input_svf(output: Output, file: io.BufferedReader) -> io.BufferedReader:
    with file:  # ensure this stays open until we're done so it doesn't get deleted...
        # Bit of weirdness here, the underlying code needs the file to be text...
        inname = file.name

        try:
            infile = open(inname, "r")
        except PermissionError:
            # _Probably_ on Windows, where it doesn't matter anyway...
            infile = file

        return svf2xsvf(output=output, infile=infile)
