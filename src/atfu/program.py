import atfu.erase
from atfu.little_board.jtag_programmer import JtagProgrammer


def handler(args):
    if args.erase or args.force:
        erase_result = atfu.erase.perform_erase(args)
        if erase_result != 0:
            exit(erase_result)

    prog = JtagProgrammer("PROGRAM", args.programmer, _verbosity(args))

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
