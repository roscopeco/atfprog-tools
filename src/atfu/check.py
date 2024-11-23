from atfu.little_board.jtag_programmer import JtagProgrammer
from atfu.standard_vectors import OP_CHECK, find_vector_file
from atfu.output import Output
from atfu.device_id import check_chip_id


def handler(args):
    exit(perform_check(args))


def perform_check(args, reuse_serial=None) -> int:
    output = Output(args)

    vector_path = find_vector_file(OP_CHECK, args.device)

    if vector_path is None:
        output.error("Failure", f"{args.device} is not a recognised device.")
        return 10

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

    if not check_chip_id(args, output, reuse_serial=reuse_serial):
        output.error(args.device, "not found, please check device type and connection")
        return 1

    prog = JtagProgrammer(
        "CHECK",
        args.programmer,
        output.verbosity(),
        no_filename=True,
        no_success=True,
        no_fail=True,
        reuse_serial=reuse_serial,
    )

    if prog.upload_one_file(vector_fd):
        output.success(args.device, "is blank")
        return 0
    else:
        output.expected_failure(args.device, "is not blank")
        return 1
