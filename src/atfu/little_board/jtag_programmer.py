import os
import string
import time
import serial
import sys

import serial.serialutil

from progress.bar import Bar
from tqdm import tqdm

if sys.stdout.isatty():
    cbWhite = "\x1b[1;37m"
    cbRed = "\x1b[1;31m"
    cbGreen = "\x1b[1;32m"
    cbYellow = "\x1b[1;33m"
    cReset = "\x1b[0m"
else:
    cbWhite = ""
    cbRed = ""
    cbGreen = ""
    cbYellow = ""
    cReset = ""


class JtagProgrammer(object):
    MODE_NORMAL = b"G"
    MODE_HIVPP = b"H"

    _translate_str_1 = "".join(
        [(chr(x) in string.printable) and chr(x) or "." for x in range(256)]
    )
    _translate_str = bytes(_translate_str_1, "ascii")

    def __init__(
        self,
        operation: str,
        device: str,
        verbosity=0,
        no_filename=False,
        no_fail=False,
        no_success=False,
        reuse_serial=None,
    ):
        self._operation = operation
        self._device = device
        self._serial = reuse_serial
        self._need_lf = False
        self._file_size = 0
        self._sum = 0
        self._start_time = 0
        self._error_code = 0
        self._verbosity = verbosity
        self._no_filename = no_filename
        self._no_fail = no_fail
        self._no_success = no_success

    def init_programmer(self, mode):
        if self._serial is None:
            self._serial = serial.Serial(port=self._device)

        self._serial.flushInput()
        self._serial.flushOutput()
        self._serial.write(mode)
        self._start_time = 0

    def serial(self):
        return self._serial

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
                if not self._no_success and self._verbosity > 1:
                    print(
                        f"{cbGreen}Success{cReset} in %.02f seconds."
                        % (time.time() - self._start_time)
                    )
            elif not self._no_fail:
                print(
                    f"{cbRed}Failure{cReset} in %.02f seconds."
                    % (time.time() - self._start_time)
                )

    def upload_one_file(self, fd, mode=MODE_NORMAL):
        try:
            self.init_programmer(mode)
        except serial.serialutil.PortNotOpenError:
            if self._verbosity > 0:
                print(
                    f"{cbRed}Failure{cReset}: Device not found, or communication failure"
                )
            return False

        self._file_size = os.fstat(fd.fileno()).st_size
        bytes_written = 0
        okquit = False

        progress = None
        if self._verbosity > 0:
            progress = tqdm(
                total=self._file_size,
                desc=f"{cbWhite}%-10s{cReset}" % self._operation,
                unit="b",
            )

        while True:
            line = self._serial.readline().strip()

            if not line:
                continue

            command = chr(line[0])
            argument = line[1:].decode("ascii")

            if command == "S":
                # Send data
                try:
                    num_bytes = int(
                        argument
                    )  # Blindly try to continue; _should_ only happen
                    # when programmer has trace debug on and is dumping an
                    # XCOMMENT(STATE)
                except Exception:
                    print(
                        f"{cbYellow}WARN{cReset}: Invalid 'S' command from programmer; Skipped..."
                    )
                    continue

                xsvf_data = fd.read(num_bytes)
                bytes_written += len(xsvf_data)
                self.update_hashes(xsvf_data)
                xsvf_data += b"\xFF" * (num_bytes - len(xsvf_data))
                self._serial.write(xsvf_data)
                if self._verbosity > 0:
                    progress.update(n=num_bytes)

            elif command == "R":
                # Ready
                self.initialize_hashes()
                if self._verbosity > 1 and not self._no_filename:
                    print("File: %s" % os.path.realpath(fd.name))
                self._start_time = time.time()

            elif command == "Q":
                # Quit (maybe error)
                if not okquit:
                    okquit = True
                    continue

                if self._verbosity > 0:
                    progress.close()

                # first field is the error code, second is the message.
                args = argument.split(",")
                self._error_code = int(args[0])
                if self._verbosity > 1:
                    print("Quit: {1:s} ({0:d}).".format(self._error_code, args[1]))
                self.print_hashes(self._error_code == 0)
                return self._error_code == 0

            elif command == "D":
                # Debug
                if self._verbosity > 1:
                    self.print_lf()
                    print("Device:", argument)

            elif command == "!":
                # Important
                if self._verbosity > 1:
                    # Can close this here, programmer only importants when done...
                    #
                    # (unless built with trace but that'll only be internal anyhow...)
                    progress.close()

                    self.print_lf()
                    print(f"{cbGreen}>>>{cReset} ", argument)

            else:
                self.print_lf()
                print(
                    "Unknown command from programmer:",
                    line.translate(JtagProgrammer._translate_str),
                )

    def upload_all_files(self, fd_list):
        ok = True
        for fd in fd_list:
            with fd:
                ok = self.upload_one_file(fd)
                if not ok:
                    break
        return ok
