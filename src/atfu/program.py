import io
import re
import os.path
import atfu.erase
from atfu.output import Output
from atfu.little_board.jtag_programmer import JtagProgrammer
from atfu.converter.jed2svf import jed2svf
from atfu.converter.svf2xsvf import svf2xsvf


def handler(args):
    output = Output(args)

    if args.erase or args.force:
        erase_result = atfu.erase.perform_erase(args)
        if erase_result != 0:
            exit(erase_result)

    prog = JtagProgrammer("PROGRAM", args.programmer, output.verbosity())

    xsvf_files = _process_input_files(args.device, args.filename, output)
    if prog.upload_all_files(xsvf_files):
        exit(0)
    else:
        exit(1)


def _process_input_files(
    device: str, files: list[io.BufferedReader], output: Output
) -> list[io.BufferedReader]:
    return [_process_input_file(device, result_file, output) for result_file in files]


def _process_input_file(device: str, file: io.BufferedReader, output: Output):
    if re.search(r"[Jj][Ee][Dd]$", file.name):
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
    return jed2svf(device=device, infile=file, output=output)


def _process_input_svf(output: Output, file: io.BufferedReader) -> io.BufferedReader:
    with file:  # ensure this stays open until we're done so it doesn't get deleted...
        # Bit of weirdness here, the underlying code needs the file to be text...
        inname = file.name
        infile = open(inname, "r")

        return svf2xsvf(output=output, infile=infile)
