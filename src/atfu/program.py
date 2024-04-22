import os
import string
import sys
import time
import serial

if sys.stdout.isatty():
    cbRed = "\x1b[1;31m"
    cbGreen = "\x1b[1;32m"
    cReset = "\x1b[0m"
else:
    cbRed = ""
    cbGreen = ""
    cReset = ""


class Programmer(object):
    MODE_NORMAL = b"G"
    MODE_HIVPP = b"H"

    _translate_str_1 = "".join(
        [(chr(x) in string.printable) and chr(x) or "." for x in range(256)]
    )
    _translate_str = bytes(_translate_str_1, "ascii")

    def __init__(self, device: str, verbosity=0):
        self._serial = serial.Serial(port=device)
        self._need_lf = False
        self._file_size = 0
        self._sum = 0
        self._start_time = 0
        self._error_code = 0
        self._verbosity = verbosity

    def init_programmer(self, mode=MODE_NORMAL):
        self._serial.flushInput()
        self._serial.flushOutput()
        self._serial.write(mode)
        self._start_time = 0

    def print_lf(self):
        if self._need_lf:
            self._need_lf = False
            print()

    def initialize_hashes(self):
        self._sum = 0

    def update_hashes(self, s):
        for c in s:
            self._sum += c

    def print_hashes(self, success: bool):
        cksum = (-self._sum) & 0xFF
        if self._verbosity > 1:
            print("  Expected checksum:  0x%02X/%lu." % (cksum, self._file_size))
            print("  Expected sum: 0x%08lX/%lu." % (self._sum, self._file_size))

        if self._start_time > 0 and self._verbosity > 0:
            if success:
                print(
                    f"{cbGreen}Success{cReset} in %.02f seconds."
                    % (time.time() - self._start_time)
                )
            else:
                print(
                    f"{cbRed}Failure{cReset} in %.02f seconds."
                    % (time.time() - self._start_time)
                )

    def upload_one_file(self, fd):
        self.init_programmer()
        self._file_size = os.fstat(fd.fileno()).st_size
        bytes_written = 0
        okquit = False
        while True:
            line = self._serial.readline().strip()

            if not line:
                continue

            command = chr(line[0])
            argument = line[1:].decode("ascii")

            match command:
                case "S":
                    # Send data
                    num_bytes = int(argument)
                    xsvf_data = fd.read(num_bytes)
                    bytes_written += len(xsvf_data)
                    self.update_hashes(xsvf_data)
                    xsvf_data += b"\xFF" * (num_bytes - len(xsvf_data))
                    self._serial.write(xsvf_data)
                    if self._verbosity > 0:
                        print(
                            "\rSent: %8d bytes, %8d remaining"
                            % (bytes_written, self._file_size - bytes_written),
                            end="",
                        )
                        sys.stdout.flush()
                        self._need_lf = True

                case "R":
                    # Ready
                    self.initialize_hashes()
                    if self._verbosity > 0:
                        print("File: %s" % os.path.realpath(fd.name))
                    self._start_time = time.time()

                case "Q":
                    # Quit (maybe error)
                    if not okquit:
                        okquit = True
                        continue
                    self.print_lf()

                    # first field is the error code, second is the message.
                    args = argument.split(",")
                    self._error_code = int(args[0])
                    if self._verbosity > 1:
                        print("Quit: {1:s} ({0:d}).".format(self._error_code, args[1]))
                    self.print_hashes(self._error_code == 0)
                    return self._error_code == 0

                case "D":
                    # Device
                    if self._verbosity > 1:
                        self.print_lf()
                        print("Device:", argument)

                case "!":
                    # Debug / important
                    if self._verbosity > 1:
                        self.print_lf()
                        print(f"{cbGreen}>>>{cReset} ", argument)

                case _:
                    self.print_lf()
                    print(
                        "Unknown command from programmer:",
                        line.translate(Programmer._translate_str),
                    )

    def upload_all_files(self, fd_list):
        ok = True
        for fd in fd_list:
            with fd:
                ok = self.upload_one_file(fd)
                if not ok:
                    break
        return ok


def handler(args):
    prog = Programmer(args.programmer, _verbosity(args))

    if prog.upload_all_files(args.filename):
        exit(0)
    else:
        exit(1)


def _verbosity(args):
    if args.quiet:
        return 0

    if args.trace:
        return 100

    if args.verbose:
        return 2

    return 1
