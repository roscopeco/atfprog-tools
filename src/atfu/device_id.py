import tempfile

from atfu.output import Output, cbYellow, cReset
from atfu.little_board.jtag_programmer import JtagProgrammer
from atfu.converter.jed2svf import jed2svf
from atfu.converter.svf2xsvf import svf2xsvf
from atfu.converter.fuseconv import write_svf
from atfu.converter.device import device_from_str
from atfu.converter.device import (
    ATF1502ASDevice,
    ATF1504ASDevice,
    ATF1508ASDevice,
    ATF1502ASVDevice,
    ATF1504ASVDevice,
    ATF1508ASVDevice,
)


def handler(args):
    output = Output(args)

    scan_result = scan_device(args, output)

    if scan_result is None:
        if not args.plain:
            output.expected_failure(
                "Scan failed", "Unsupported device, no device or communication error"
            )
        exit(1)
    else:
        if args.plain:
            print(scan_result, end="")
        else:
            output.success(scan_result, "device detected successfully")

        exit(0)


def check_chip_id(args: any, output: Output, device: str | None = None) -> bool:
    if device is None:
        device = args.device

    c_device = device_from_str(device)
    if c_device is None:
        output.error(
            "Bug",
            f"Incorrect device string {device} passed in jed2svf; Please report: https://github.com/roscopeco/atfprog-tools/issues",
        )
        exit(1000)

    temp_svf = tempfile.NamedTemporaryFile(
        prefix="atfu-temp-", suffix=".svf", mode="w+"
    )

    # Calling without erase, verify or program true will just do device id verification...
    write_svf(
        temp_svf,
        svf_bits=None,
        device=c_device,
        comment="ID check",
        erase=False,
        verify=False,
        program=False,
    )

    temp_svf.seek(0)

    temp_xsvf = svf2xsvf(output=output, infile=temp_svf)

    prog = JtagProgrammer(
        "ID",
        args.programmer,
        verbosity=0,
        no_success=True,
        no_fail=True,
        no_filename=True,
    )

    return prog.upload_all_files([temp_xsvf])


def scan_device(args: any, output: Output) -> str | None:
    if check_chip_id(args, output, "ATF1502AS"):
        return "ATF1502AS"
    if check_chip_id(args, output, "ATF1504AS"):
        return "ATF1504AS"
    if check_chip_id(args, output, "ATF1508AS"):
        return "ATF1508AS"
    if check_chip_id(args, output, "ATF1502ASV"):
        return "ATF1502ASV"
    if check_chip_id(args, output, "ATF1504ASV"):
        return "ATF1504ASV"
    if check_chip_id(args, output, "ATF1508ASV"):
        return "ATF1508ASV"

    return None
