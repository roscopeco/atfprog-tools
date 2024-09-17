import argparse
import re

from atfu.converter.jesd3 import JESD3Parser
from atfu.converter.svfeventhandler import SVFEventHandler
from atfu.converter.device import ATF15xxInstr


def read_jed(file):
    jed = file.read()

    # TODO
    #
    # CUPL will emit weird test vectors (with the max vector QV number *after* the
    # first V0001, which _seems_ to be off-spec. The jesd3 code can't handle this.
    #
    # We don't care about test vectors anyway, but we need to at least be able to
    # checksum them, so for now we'll just refuse to process a jed that has vectors
    # in it...
    #
    # Leaving the regexes below in case they're useful late (to be able to just
    # remove the problem vectors **by force**). See also jesd3.py:
    #
    # jed = re.sub(r'\r?\nQV[0-9]+\*', '', jed)
    # jed = re.sub(r'V[0-9+][^\r\n]+\r?\n?\*?', '', jed)

    parser = JESD3Parser(jed)
    parser.parse()
    return parser.fuse, parser.design_spec


class ATFSVFEventHandler(SVFEventHandler):
    def ignored(self, *args, **kwargs):
        pass

    svf_frequency = ignored
    svf_trst = ignored
    svf_state = ignored
    svf_endir = ignored
    svf_enddr = ignored
    svf_hir = ignored
    # svf_sir = ignored
    svf_tir = ignored
    svf_hdr = ignored
    # svf_sdr = ignored
    svf_tdr = ignored
    # svf_runtest = ignored
    svf_piomap = ignored
    svf_pio = ignored

    def __init__(self):
        self.ir = None
        self.erase = False
        self.addr = 0
        self.data = b""
        self.bits = {}

    # def svf_sir(self, tdi, smask, tdo, mask):
    #     self.ir = int.from_bytes(tdi.tobytes(), "little")
    #     if self.ir == ATF15xxInstr.ISC_LATCH_ERASE:
    #         self.erase = True
    #     if self.ir == ATF15xxInstr.ISC_DATA:
    #         self.erase = False

    # def svf_sdr(self, tdi, smask, tdo, mask):
    #     if self.ir == ATF15xxInstr.ISC_ADDRESS:
    #         self.addr = int.from_bytes(tdi.tobytes(), "little")
    #     if (self.ir & ~0x3) == ATF15xxInstr.ISC_DATA:
    #         self.data = tdi

    # def svf_runtest(
    #     self, run_state, run_count, run_clock, min_time, max_time, end_state
    # ):
    #     if not self.erase and self.ir == ATF15xxInstr.ISC_PROGRAM_ERASE:
    #         self.bits[self.addr] = self.data


def write_svf(
    file, svf_bits, device, *, comment, erase=False, program=True, verify=True
):
    # This code is kind of awful.
    def emit_header():
        for comment_line in comment.splitlines():
            file.write("// {}\n".format(comment_line))
        file.write("TRST ABSENT;\n")
        file.write("ENDIR IDLE;\n")
        file.write("ENDDR IDLE;\n")
        file.write("HDR 0;\n")
        file.write("HIR 0;\n")
        file.write("TDR 0;\n")
        file.write("TIR 0;\n")
        file.write("STATE RESET;\n")

    def emit_check_idcode(idcode):
        file.write("// Check IDCODE\n")
        file.write("SIR 10 TDI ({:03x});\n".format(ATF15xxInstr.IDCODE))
        file.write(
            "SDR 32 TDI (ffffffff)\n\tTDO ({:08x})\n\tMASK (ffffffff);\n".format(idcode)
        )

    def emit_enable():
        file.write("// ISC enable\n")
        file.write("SIR 10 TDI ({:03x});\n".format(ATF15xxInstr.ISC_CONFIG))
        file.write("SDR 10 TDI ({:03x});\n".format(0x1B9))  # magic constant?
        file.write("STATE IDLE;\n")

    def emit_disable():
        file.write("// ISC disable\n")
        file.write("SIR 10 TDI ({:03x});\n".format(ATF15xxInstr.ISC_CONFIG))
        file.write("SDR 10 TDI ({:03x});\n".format(0x000))
        file.write("STATE IDLE;\n")

    def emit_unknown():
        # ATMISP does this for unknown reasons. DR seems to be just BYPASS. Removing this
        # doesn't do anything (and shouldn't do anything, since ATMISP doesn't go through RTI
        # or capture/update DR), but let's keep it for now. Vendor tools wouldn't emit SIR
        # without any reason whatsoever, right? Right??
        file.write("// ISC unknown\n")
        file.write("SIR 10 TDI ({:03x});\n".format(ATF15xxInstr.ISC_UNKNOWN))

    def emit_erase():
        file.write("// ISC erase\n")
        file.write("SIR 10 TDI ({:03x});\n".format(ATF15xxInstr.ISC_LATCH_ERASE))
        file.write("SIR 10 TDI ({:03x});\n".format(ATF15xxInstr.ISC_PROGRAM_ERASE))
        file.write("RUNTEST IDLE 210E-3 SEC;\n")
        emit_unknown()

    def emit_program(address, data):
        file.write("// ISC program word\n")
        file.write("SIR 10 TDI ({:03x});\n".format(ATF15xxInstr.ISC_ADDRESS))
        file.write("SDR 11 TDI ({:03x});\n".format(address))
        file.write(
            "SIR 10 TDI ({:03x});\n".format(ATF15xxInstr.ISC_DATA | (address >> 8))
        )

        # TODO this is a bit of a hack...
        hexout = "{:0{}x}".format(int(data.to01()[::-1], 2), len(data) // 4)
        if (len(data) // 4) & 0x1:
            hexout = "0" + hexout

        file.write("SDR {} TDI ({});\n".format(len(data), hexout))
        file.write("SIR 10 TDI ({:03x});\n".format(ATF15xxInstr.ISC_PROGRAM_ERASE))
        file.write("RUNTEST IDLE 30E-3 SEC;\n")
        emit_unknown()

    def emit_verify(address, data):
        file.write("// ISC verify word\n")
        file.write("SIR 10 TDI ({:03x});\n".format(ATF15xxInstr.ISC_ADDRESS))
        file.write("SDR 11 TDI ({:03x});\n".format(address))
        file.write("SIR 10 TDI ({:03x});\n".format(ATF15xxInstr.ISC_READ))
        file.write("RUNTEST IDLE 20E-3 SEC;\n")
        file.write(
            "SIR 10 TDI ({:03x});\n".format(ATF15xxInstr.ISC_DATA | (address >> 8))
        )

        # TODO this is the same hack as above...
        hexout = "{:0{}x}".format(int(data.to01()[::-1], 2), len(data) // 4)
        if (len(data) // 4) & 0x1:
            hexout = "0" + hexout

        file.write(
            "SDR {} TDI ({})\n\tTDO ({})\n\tMASK ({:0{}x});\n".format(
                len(data),
                hexout,
                hexout,
                (1 << len(data)) - 1,
                len(data) // 4,
            )
        )

    emit_header()
    emit_check_idcode(device.idcode)
    emit_enable()

    if erase:
        emit_erase()

    if program:
        for svf_row in svf_bits:
            emit_program(svf_row, svf_bits[svf_row])

    if verify:
        for svf_row in svf_bits:
            emit_verify(svf_row, svf_bits[svf_row])

    emit_disable()


class ATFFileType(argparse.FileType):
    def __call__(self, value):
        file = super().__call__(value)
        filename = file.name.lower()
        if not filename.endswith(".jed"):
            raise argparse.ArgumentTypeError("{} is not a JED file".format(filename))
        return file
