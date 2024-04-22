import serial.tools.list_ports
from tabulate import tabulate

OUR_VID = 0x04D8
OUR_PID = 0xE5C7


def handle_list(args):
    if args.plain:
        _list_plain(find_programmers())
    else:
        _list_detail(find_programmers())


def _list_plain(programmers: list[list[str]]) -> None:
    for programmer in programmers:
        print(programmer["Device"])


def _list_detail(programmers: list[list[str]]) -> None:
    print()
    if programmers:
        print(f"Found {len(programmers)} programmer(s):")
        print()
        print(tabulate(programmers, headers="keys", showindex=True))
        print()
        print(
            "Unless specified (with the -p option), ",
            f"{programmers[0]['Device']} will be used",
        )
        print("for programming and related operations.")
    else:
        print("No programmers found!")
    print()


def handle_query(args):
    print("Query handler")


def find_programmers() -> list[dict[str, str]]:
    all_progs = serial.tools.list_ports.comports(False)
    return [
        {
            "Device": prog.device,
            "Product": prog.product,
            "Manufacturer": prog.manufacturer,
        }
        for prog in all_progs
        if prog.vid == OUR_VID and prog.pid == OUR_PID
    ]


def default_programmer() -> dict[str, str] | None:
    default = find_programmers()[0:1]
    if default:
        return default[0]
    else:
        return None


def default_programmer_path() -> str | None:
    default = default_programmer()
    if default:
        return default["Device"]
    else:
        return None
