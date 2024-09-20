import argparse
import serial

import sure
from unittest.mock import patch, MagicMock

from atfu.check import perform_check


def test_check_perform_check_no_device():
    args = argparse.Namespace(
        quiet=False,
        trace=False,
        verbose=False,
        force=False,
        programmer="/dev/programmer",
        device=None,
    )

    result = perform_check(args)

    result.should.be.equal_to(10)


def test_check_perform_check_unrecognised_device():
    args = argparse.Namespace(
        quiet=False,
        trace=False,
        verbose=False,
        force=False,
        programmer="/dev/programmer",
        device="ATF1024",
    )

    result = perform_check(args)

    result.should.be.equal_to(10)


@patch.multiple(
    "atfu.check.JtagProgrammer",
    upload_all_files=MagicMock(return_value=True),
    upload_one_file=MagicMock(return_value=True),
)
def test_check_perform_check_valid_device_check_ok():
    args = argparse.Namespace(
        quiet=False,
        trace=False,
        verbose=False,
        force=False,
        programmer="/dev/programmer",
        device="ATF1502",
    )

    result = perform_check(args)

    result.should.be.equal_to(0)


@patch.multiple(
    "atfu.check.JtagProgrammer",
    upload_all_files=MagicMock(return_value=True),
    upload_one_file=MagicMock(return_value=False),
)
def test_check_perform_check_valid_device_check_fails():
    args = argparse.Namespace(
        quiet=False,
        trace=False,
        verbose=False,
        force=False,
        programmer="/dev/programmer",
        device="ATF1502",
    )

    result = perform_check(args)

    result.should.be.equal_to(1)


@patch.multiple(
    "atfu.check.JtagProgrammer",
    upload_all_files=MagicMock(return_value=False),
    upload_one_file=MagicMock(return_value=True),
)
def test_check_perform_check_invalid_device():
    args = argparse.Namespace(
        quiet=False,
        trace=False,
        verbose=False,
        force=False,
        programmer="/dev/programmer",
        device="ATF1502",
    )

    result = perform_check(args)

    result.should.be.equal_to(1)
