import argparse
import serial

import sure
from unittest.mock import patch, MagicMock

from atfu.erase import perform_erase


def test_erase_perform_erase_no_device():
    args = argparse.Namespace(
        quiet=False,
        trace=False,
        verbose=False,
        force=False,
        programmer="/dev/programmer",
        device=None,
    )

    result = perform_erase(args)

    result.should.be.equal_to(10)


def test_erase_perform_erase_unrecognised_device():
    args = argparse.Namespace(
        quiet=False,
        trace=False,
        verbose=False,
        force=False,
        programmer="/dev/programmer",
        device="ATF1024",
    )

    result = perform_erase(args)

    result.should.be.equal_to(10)


@patch.multiple(
    "atfu.check.JtagProgrammer",
    upload_all_files=MagicMock(return_value=True),
    upload_one_file=MagicMock(return_value=True),
)
def test_erase_perform_erase_valid_device_erase_ok():
    args = argparse.Namespace(
        quiet=False,
        trace=False,
        verbose=False,
        force=False,
        programmer="/dev/programmer",
        device="ATF1502",
    )

    result = perform_erase(args)

    result.should.be.equal_to(0)


@patch.multiple(
    "atfu.check.JtagProgrammer",
    upload_all_files=MagicMock(return_value=True),
    upload_one_file=MagicMock(return_value=False),
)
def test_erase_perform_erase_valid_device_erase_fails():
    args = argparse.Namespace(
        quiet=False,
        trace=False,
        verbose=False,
        force=False,
        programmer="/dev/programmer",
        device="ATF1502",
    )

    result = perform_erase(args)

    result.should.be.equal_to(1)


@patch.multiple(
    "atfu.check.JtagProgrammer",
    upload_all_files=MagicMock(return_value=True),
    upload_one_file=MagicMock(return_value=False),
)
def test_erase_perform_erase_valid_device_force_erase_fails_fails():
    args = argparse.Namespace(
        quiet=False,
        trace=False,
        verbose=False,
        force=True,
        programmer="/dev/programmer",
        device="ATF1502",
    )

    result = perform_erase(args)

    result.should.be.equal_to(1)


@patch.multiple(
    "atfu.check.JtagProgrammer",
    upload_all_files=MagicMock(return_value=True),
    upload_one_file=MagicMock(side_effect=[False, True]),
)
def test_erase_perform_erase_valid_device_force_erase_fails_succeeds():
    args = argparse.Namespace(
        quiet=False,
        trace=False,
        verbose=False,
        force=True,
        programmer="/dev/programmer",
        device="ATF1502",
    )

    result = perform_erase(args)

    result.should.be.equal_to(0)


@patch.multiple(
    "atfu.check.JtagProgrammer",
    upload_all_files=MagicMock(return_value=False),
    upload_one_file=MagicMock(return_value=True),
)
def test_check_perform_erase_invalid_device_no_force():
    args = argparse.Namespace(
        quiet=False,
        trace=False,
        verbose=False,
        force=False,
        programmer="/dev/programmer",
        device="ATF1502",
    )

    result = perform_erase(args)

    result.should.be.equal_to(1)


@patch.multiple(
    "atfu.check.JtagProgrammer",
    upload_all_files=MagicMock(return_value=False),
    upload_one_file=MagicMock(return_value=True),
)
def test_check_perform_erase_invalid_device_force():
    args = argparse.Namespace(
        quiet=False,
        trace=False,
        verbose=False,
        force=True,
        programmer="/dev/programmer",
        device="ATF1502",
    )

    result = perform_erase(args)

    result.should.be.equal_to(0)  # Cannot check device is valid when force=True
