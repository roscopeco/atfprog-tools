import argparse
import serial

import sure
from unittest.mock import patch

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


@patch("atfu.check.JtagProgrammer")
def test_check_perform_check_valid_device_check_ok(mock_prog):
    prog_inst = mock_prog.return_value
    prog_inst.upload_one_file.return_value = True

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


@patch("atfu.check.JtagProgrammer")
def test_check_perform_check_valid_device_check_fails(mock_prog):
    prog_inst = mock_prog.return_value
    prog_inst.upload_one_file.return_value = False

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
