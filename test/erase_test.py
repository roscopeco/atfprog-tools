import sure
from unittest.mock import patch

from atfu.erase import handler


@patch("serial.tools.list_ports.comports")
def test_programmer_find_programmers_none(patched_comports):
    pass
