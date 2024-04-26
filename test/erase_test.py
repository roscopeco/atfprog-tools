import argparse
import serial

import sure
from unittest.mock import patch

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


@patch("atfu.erase.JtagProgrammer")
def test_erase_perform_erase_valid_device_erase_ok(mock_prog):
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

    result = perform_erase(args)

    result.should.be.equal_to(0)


@patch("atfu.erase.JtagProgrammer")
def test_erase_perform_erase_valid_device_erase_fails(mock_prog):
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

    result = perform_erase(args)

    result.should.be.equal_to(1)


@patch("atfu.erase.JtagProgrammer")
def test_erase_perform_erase_valid_device_force_erase_fails_fails(mock_prog):
    prog_inst = mock_prog.return_value
    prog_inst.upload_one_file.return_value = False

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


@patch("atfu.erase.JtagProgrammer")
def test_erase_perform_erase_valid_device_force_erase_fails_succeeds(mock_prog):
    prog_inst = mock_prog.return_value
    prog_inst.upload_one_file.side_effect = [False, True]

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
