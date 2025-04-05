from atfu.little_board.jtag_programmer import JtagProgrammer
from atfu.standard_vectors import OP_ERASE, find_vector_file
from atfu.output import Output
from atfu.device_id import check_chip_id


def handler(args):
    exit(perform_erase(args))


def perform_erase(args, no_success=True, reuse_serial=None) -> int:
    output = Output(args)

    vector_path = find_vector_file(OP_ERASE, args.device)

    if vector_path is None:
        output.error("Failure", f"{args.device} is not a recognised device.")
        return 10

    if args.force:
        output.warn(args.device, "assumed correct; cannot check when force-erasing")
    else:
        if not check_chip_id(args, output, reuse_serial=reuse_serial):
            output.error(
                args.device, "not found, please check device type and connection"
            )
            return 1

    try:
        vector_fd = vector_path.open("rb")
    except FileNotFoundError:
        output.error(
            "Failure", f"Support for {args.device} is not installed correctly."
        )
        output.error(
            "       ", "Please check your installation and reinstall if necessary."
        )
        return 2

    if args.force:
        prog = JtagProgrammer(
            "ERASE-1",
            args.programmer,
            output.verbosity(),
            no_filename=True,
            no_fail=True,
            no_success=no_success,
            reuse_serial=reuse_serial,
        )
        ok = prog.upload_one_file(vector_fd, JtagProgrammer.MODE_HIVPP)
        if not ok:
            prog = JtagProgrammer(
                "ERASE-2",
                args.programmer,
                output.verbosity(),
                no_filename=True,
                no_success=no_success,
                reuse_serial=reuse_serial,
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
            output.verbosity(),
            no_filename=True,
            no_success=no_success,
            reuse_serial=reuse_serial,
        )
        if prog.upload_one_file(vector_fd, JtagProgrammer.MODE_NORMAL):
            return 0
        else:
            return 1
