import sys
from atfu.little_board.jtag_programmer import JtagProgrammer
from atfu.standard_vectors import OP_ERASE, find_vector_file

# TODO these are duplicated, factor them out...
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


def handler(args):
    exit(perform_erase(args))


def perform_erase(args, no_success=True) -> int:
    verbosity = _verbosity(args)
    vector_path = find_vector_file(OP_ERASE, args.device)

    if vector_path is None:
        if verbosity > 0:
            print(f"{cbRed}Failure{cReset}: {args.device} is not a recognised device.")
        return 1

    try:
        vector_fd = vector_path.open("rb")
    except FileNotFoundError:
        if verbosity > 0:
            print(
                f"{cbRed}Failure{cReset}: Support for {args.device} is not installed correctly."
            )
            print("Please check your installation and reinstall if necessary.")
        return 2

    if args.force:
        prog = JtagProgrammer(
            "ERASE-1",
            args.programmer,
            _verbosity(args),
            no_filename=True,
            no_fail=True,
            no_success=no_success,
        )
        ok = prog.upload_one_file(vector_fd, JtagProgrammer.MODE_HIVPP)
        if not ok:
            prog = JtagProgrammer(
                "ERASE-2",
                args.programmer,
                _verbosity(args),
                no_filename=True,
                no_success=no_success,
            )
            if not prog.upload_one_file(vector_fd, JtagProgrammer.MODE_NORMAL):
                return 1
            else:
                return 0
        else:
            return 0
    else:
        prog = JtagProgrammer(
            "ERASE",
            args.programmer,
            _verbosity(args),
            no_filename=True,
            no_success=no_success,
        )
        prog.upload_one_file(vector_fd, JtagProgrammer.MODE_HIVPP)
        return 0


def _verbosity(args):
    if args.quiet:
        return 0

    if args.trace:
        return 100

    if args.verbose:
        return 2

    return 1
