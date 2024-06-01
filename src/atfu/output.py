import sys

if sys.stdout.isatty():
    cbRed = "\x1b[1;31m"
    cbGreen = "\x1b[1;32m"
    cbYellow = "\x1b[1;33m"
    cReset = "\x1b[0m"
else:
    cbRed = ""
    cbGreen = ""
    cbYellow = ""
    cReset = ""

the_output = None


class Output:
    def __init__(self, args):
        global the_output
        self._verbosity = self._verbosity(args)
        the_output = self

    def verbosity(self):
        return self._verbosity

    def output(self, level: int, msg: str):
        if self._verbosity > level:
            print(msg)

    def error(self, title: str, msg: str):
        self.output(0, f"{cbRed}{title}{cReset}: {msg}")

    def warn(self, title: str, msg: str):
        self.output(1, f"{cbYellow}{title}{cReset}: {msg}")

    def success(self, title: str, msg: str):
        self.output(0, f"{cbGreen}{title}{cReset}: {msg}")

    def expected_failure(self, title: str, msg: str):
        self.output(0, f"{cbRed}{title}{cReset}: {msg}")

    def _verbosity(self, args):
        if args.quiet:
            return 0

        if args.trace:
            return 100

        if args.verbose:
            return 2

        return 1


def global_output() -> Output:
    return the_output
