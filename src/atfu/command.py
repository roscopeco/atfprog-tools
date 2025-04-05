import argparse

import atfu.device_id
import atfu.program
import atfu.erase
import atfu.check
import atfu.verify
import atfu.programmer

BOARDNAME = "Little ATF150x Programmer Board"
PROGNAME = f"{BOARDNAME} Utility"
VERSION = "2025.1024"


def main():
    args = _arg_parser().parse_args()
    args.func(args)


def _arg_parser():
    parser = argparse.ArgumentParser(description=f"{PROGNAME}")
    parser.add_argument(
        "--version",
        action="version",
        version=f"{PROGNAME} v{VERSION}; (c) The Really Old-School Company Ltd",
    )
    parser.add_argument(
        "-q", "--quiet", action="store_true", help="Silence almost all output"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Allow additional output"
    )
    parser.add_argument(
        "-t",
        "--trace",
        action="store_true",
        help="Enable debugging output (can be noisy!)",
    )

    subs = parser.add_subparsers(dest="{program,erase,check,programmer}", required=True)

    # Scan
    scan = subs.add_parser("scan", help=f"Scan for ATF150x devices")
    scan.add_argument(
        "-n",
        "--plain",
        action="store_true",
        help="Plain output, only the unadorned device name, no newline",
    )
    scan.add_argument(
        "-p",
        "--programmer",
        default=atfu.programmer.default_programmer_path(),
        help="Programmer device (default: %(default)s)",
    )
    scan.set_defaults(func=atfu.device_id.handler)

    # Program
    program = subs.add_parser("program", help="Program an ATF150x device")
    program.add_argument(
        "-e", "--erase", action="store_true", help="Erase before programming"
    )
    program.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="Force-erase before programming (implies -e)",
    )
    program.add_argument(
        "-n",
        "--noverify",
        action="store_true",
        help="Skip verification after programming",
    )
    program.add_argument(
        "-d",
        "--device",
        default="ATF1502AS",
        choices=(
            "ATF1502",
            "ATF1504",
            "ATF1508",
            "ATF1502AS",
            "ATF1504AS",
            "ATF1508AS",
            "ATF1502ASV",
            "ATF1504ASV",
            "ATF1508ASV",
        ),
        help="Device to program (default: %(default)s)",
    )
    program.add_argument(
        "-p",
        "--programmer",
        default=atfu.programmer.default_programmer_path(),
        help="Programmer device (default: %(default)s)",
    )
    program.add_argument(
        "filename",
        nargs="+",
        type=argparse.FileType("rb"),
        help=".jed, .svf or .xsvf file(s) to program",
    )
    program.set_defaults(func=atfu.program.handler)

    # Erase
    erase = subs.add_parser("erase", help="Erase an ATF150x device")
    erase.add_argument("-f", "--force", action="store_true", help="Force erase")
    erase.add_argument(
        "-p",
        "--programmer",
        default=atfu.programmer.default_programmer_path(),
        help="Programmer device (default: %(default)s)",
    )
    erase.add_argument(
        "-d",
        "--device",
        default="ATF1502AS",
        choices=(
            "ATF1502",
            "ATF1504",
            "ATF1508",
            "ATF1502AS",
            "ATF1504AS",
            "ATF1508AS",
            "ATF1502ASV",
            "ATF1504ASV",
            "ATF1508ASV",
        ),
        help="Device to erase (default: %(default)s)",
    )
    erase.set_defaults(func=atfu.erase.handler)

    # Check
    check = subs.add_parser("check", help="Check if an ATF150x device is blank")
    check.add_argument(
        "-p",
        "--programmer",
        default=atfu.programmer.default_programmer_path(),
        help="Programmer device (default: %(default)s)",
    )
    check.add_argument(
        "-d",
        "--device",
        default="ATF1502AS",
        choices=(
            "ATF1502",
            "ATF1504",
            "ATF1508",
            "ATF1502AS",
            "ATF1504AS",
            "ATF1508AS",
            "ATF1502ASV",
            "ATF1504ASV",
            "ATF1508ASV",
        ),
        help="Device to check (default: %(default)s)",
    )
    check.set_defaults(func=atfu.check.handler)

    # Verify
    verify = subs.add_parser("verify", help="Verify an ATF150x device")
    verify.add_argument(
        "-d",
        "--device",
        default="ATF1502AS",
        choices=(
            "ATF1502",
            "ATF1504",
            "ATF1508",
            "ATF1502AS",
            "ATF1504AS",
            "ATF1508AS",
            "ATF1502ASV",
            "ATF1504ASV",
            "ATF1508ASV",
        ),
        help="Device to verify (default: %(default)s)",
    )
    verify.add_argument(
        "-p",
        "--programmer",
        default=atfu.programmer.default_programmer_path(),
        help="Programmer device (default: %(default)s)",
    )
    verify.add_argument(
        "filename",
        nargs="+",
        type=argparse.FileType("rb"),
        help=".jed file(s) to verify against",
    )
    verify.set_defaults(func=atfu.verify.handler)

    # Programmer
    programmer = subs.add_parser("programmer", help=f"{BOARDNAME} device functions")

    programmer_subs = programmer.add_subparsers(required=True)

    programmer_list = programmer_subs.add_parser(
        "list", description="Functions for listing connected programmers"
    )
    programmer_list.add_argument(
        "-n",
        "--plain",
        action="store_true",
        help="Display a plain list of device paths",
    )
    programmer_list.set_defaults(func=atfu.programmer.handle_list)

    programmer_query = programmer_subs.add_parser(
        "query", description="Functions for querying connected programmers"
    )
    programmer_query.add_argument(
        "-p",
        "--programmer",
        default=atfu.programmer.default_programmer_path(),
        help="Programmer device to query (default: %(default)s)",
    )
    programmer_query.set_defaults(func=atfu.programmer.handle_query)

    return parser


if __name__ == "__main__":
    main()
