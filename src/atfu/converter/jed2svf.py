import io
import tempfile
from atfu.output import Output
from atfu.converter.fuseconv import read_jed, write_svf
from atfu.converter.device import (
    ATF1502ASDevice,
    ATF1504ASDevice,
    ATF1508ASDevice,
    ATF1502ASVDevice,
    ATF1504ASVDevice,
    ATF1508ASVDevice,
)

# TODO don't be exit()ing in here.......


def jed2svf(
    output: Output,
    device: str,
    infile: io.BufferedReader,
    erase: bool,
    verify: bool,
    program: bool,
) -> io.BufferedReader:
    output.output(2, "Converting JED to SVF...")

    # Underlying code expects a text reader, not binary...
    inname = infile.name
    infile.close()
    infile = open(inname, "r")

    if device == "ATF1502AS" or device == "ATF1502":
        c_device = ATF1502ASDevice
    elif device == "ATF1504AS" or device == "ATF1504":
        c_device = ATF1504ASDevice
    elif device == "ATF1508AS" or device == "ATF1508":
        c_device = ATF1508ASDevice
    elif device == "ATF1502ASV":
        c_device = ATF1502ASVDevice
    elif device == "ATF1504ASV":
        c_device = ATF1504ASVDevice
    elif device == "ATF1508ASV":
        c_device = ATF1508ASVDevice
    else:
        output.error(
            "Bug",
            f"Incorrect device string {device} passed in jed2svf; Please report: https://github.com/roscopeco/atfprog-tools/issues",
        )
        exit(1000)

    jed_bits = svf_bits = None
    if infile.name.lower().endswith(".jed"):
        jed_bits, comment = read_jed(infile)
        if c_device.fuse_count != len(jed_bits):
            output.error(
                "Failure",
                f"Wrong number of fuses {len(jed_bits)} for device {device} (expected {c_device.fuse_count})",
            )
            exit(50)
    else:
        output.error(
            "Bug",
            "jed2svf called on non-JED; Please report: https://github.com/roscopeco/atfprog-tools/issues",
        )
        exit(1000)

    if svf_bits is None:
        svf_bits = c_device.jed_to_svf(jed_bits)

    outfile = tempfile.NamedTemporaryFile(prefix="atfu-temp-", suffix=".svf", mode="w+")
    write_svf(
        outfile,
        svf_bits,
        c_device,
        comment=comment,
        erase=erase,
        verify=verify,
        program=program,
    )

    outfile.seek(0)
    return outfile
