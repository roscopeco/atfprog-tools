from atfu.little_board.jtag_programmer import JtagProgrammer


def handler(args):
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
