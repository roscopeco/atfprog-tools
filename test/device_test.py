from serial.tools.list_ports_common import ListPortInfo

import sure
from unittest.mock import patch

from atfu.programmer import find_programmers

OUR_VID = 0x04D8
OUR_PID = 0xE5C7

OTHER_VID = 0x04D9
OTHER_PID = 0xE5C8


@patch("serial.tools.list_ports.comports")
def test_programmer_find_programmers_none(patched_comports):
    patched_comports.return_value = _fake_port_info_none()

    result = find_programmers()

    patched_comports.assert_called_with(False)
    result.should.have.length_of(0)


@patch("serial.tools.list_ports.comports")
def test_programmer_find_programmers_one_not_ours(patched_comports):
    patched_comports.return_value = _fake_port_info_one_not_ours()

    result = find_programmers()

    patched_comports.assert_called_with(False)
    result.should.have.length_of(0)


@patch("serial.tools.list_ports.comports")
def test_programmer_find_programmers_two_not_ours(patched_comports):
    patched_comports.return_value = _fake_port_info_two_not_ours()

    result = find_programmers()

    patched_comports.assert_called_with(False)
    result.should.have.length_of(0)


@patch("serial.tools.list_ports.comports")
def test_programmer_find_programmers_one_ours(patched_comports):
    patched_comports.return_value = _fake_port_info_one_ours()

    result = find_programmers()

    patched_comports.assert_called_with(False)
    result.should.have.length_of(1)


@patch("serial.tools.list_ports.comports")
def test_programmer_find_programmers_two_one_ours(patched_comports):
    patched_comports.return_value = _fake_port_info_two_one_ours()

    result = find_programmers()

    patched_comports.assert_called_with(False)
    result.should.have.length_of(1)


@patch("serial.tools.list_ports.comports")
def test_programmer_find_programmers_two_both_ours(patched_comports):
    patched_comports.return_value = _fake_port_info_two_both_ours()

    result = find_programmers()

    patched_comports.assert_called_with(False)
    result.should.have.length_of(2)


@patch("serial.tools.list_ports.comports")
def test_programmer_find_programmers_our_vid_not_pid(patched_comports):
    patched_comports.return_value = [_fake_port_info("/dev/fake0", OUR_VID, OTHER_PID)]

    result = find_programmers()

    patched_comports.assert_called_with(False)
    result.should.have.length_of(0)


@patch("serial.tools.list_ports.comports")
def test_programmer_find_programmers_our_pid_not_vid(patched_comports):
    patched_comports.return_value = [_fake_port_info("/dev/fake0", OTHER_VID, OUR_PID)]

    result = find_programmers()

    patched_comports.assert_called_with(False)
    result.should.have.length_of(0)


def _fake_port_info_none() -> list[ListPortInfo]:
    return []


def _fake_port_info_one_not_ours() -> list[ListPortInfo]:
    return [
        ListPortInfo(device="/dev/fakedevice0", skip_link_detection=True),
    ]


def _fake_port_info_two_not_ours() -> list[ListPortInfo]:
    return [
        ListPortInfo(device="/dev/fakedevice0", skip_link_detection=True),
        ListPortInfo(device="/dev/fakedevice1", skip_link_detection=True),
    ]


def _fake_port_info_one_ours() -> list[ListPortInfo]:
    return [
        _fake_port_info("/dev/fakedevice0", OUR_VID, OUR_PID),
    ]


def _fake_port_info_two_one_ours() -> list[ListPortInfo]:
    return [
        _fake_port_info("/dev/fakedevice0", OUR_VID, OUR_PID),
        _fake_port_info("/dev/fakedevice1", OTHER_VID, OTHER_PID),
    ]


def _fake_port_info_two_both_ours() -> list[ListPortInfo]:
    return [
        _fake_port_info("/dev/fakedevice0", OUR_VID, OUR_PID),
        _fake_port_info("/dev/fakedevice1", OUR_VID, OUR_PID),
    ]


def _fake_port_info(device: str, vid: int, pid: int) -> ListPortInfo:
    info = ListPortInfo(device, True)
    info.vid = vid
    info.pid = pid
    return info
