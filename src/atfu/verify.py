import io
import re
import os.path
from atfu.output import Output
from atfu.little_board.jtag_programmer import JtagProgrammer
from atfu.converter.jed2svf import jed2svf
from atfu.converter.svf2xsvf import svf2xsvf
from atfu.device_id import check_chip_id


def handler(args):
    exit(perform_verify(args))


def perform_verify(args, reuse_serial=None):
    output = Output(args)

    if not check_chip_id(args, output, reuse_serial=reuse_serial):
        output.error(args.device, "not found, please check device type and connection")
        return 1

    prog = JtagProgrammer(
        "VERIFY",
        args.programmer,
        output.verbosity(),
        no_fail=True,
        reuse_serial=reuse_serial,
    )

    xsvf_files = _process_input_files(args.device, args.filename, output)

    if prog.upload_all_files(xsvf_files):
        output.success(args.device, "verified successfully")
        return 0
    else:
        output.error(args.device, "verification failed")
        return 1


def _process_input_files(
    device: str, files: list[io.BufferedReader], output: Output
) -> list[io.BufferedReader]:
    return [_process_input_file(device, result_file, output) for result_file in files]


def _process_input_file(device: str, file: io.BufferedReader, output: Output):
    if re.search(r"[Jj][Ee][Dd]$", file.name):
        return _process_input_svf(output, _process_input_jed(output, device, file))
    elif re.search(r"[^Xx][Ss][Vv][Ff]$", file.name):
        output.error(
            "Failure",
            f"Separate verification only for JESD3-C (.jed), {os.path.basename(file.name)} is SVF; Cannot continue",
        )
        exit(89)
    elif re.search(r"[Xx][Ss][Vv][Ff]$", file.name):
        output.error(
            "Failure",
            f"Separate erification only for JESD3-C (.jed), {os.path.basename(file.name)} is XSVF; Cannot continue",
        )
        exit(89)
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
        program=False,
        verify=True,
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
