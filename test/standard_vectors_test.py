import sure
from unittest.mock import patch

from atfu.standard_vectors import (
    OP_CHECK,
    OP_ERASE,
    ATF_1502,
    ATF_1504,
    ATF_1508,
    find_vector_file,
    atf_device_key,
)


def test_find_vector_file_none_none():
    result = find_vector_file(None, None)
    result.should.be.none


def test_find_vector_file_empty_none():
    result = find_vector_file("", None)
    result.should.be.none


def test_find_vector_file_none_empty():
    result = find_vector_file(None, "")
    result.should.be.none


def test_find_vector_file_empty_empty():
    result = find_vector_file("", "")
    result.should.be.none


def test_find_vector_file_valid_empty():
    result = find_vector_file(OP_CHECK, "")
    result.should.be.none


def test_find_vector_file_empty_valid():
    result = find_vector_file("", ATF_1502)
    result.should.be.none


def test_find_vector_file_check_1502():
    result = find_vector_file(OP_CHECK, ATF_1502)
    str(result).should.match(r"src[\\/]atfu[\\/]standard_vectors[\\/]bc1502.xsvf$")


def test_find_vector_file_check_1504():
    result = find_vector_file(OP_CHECK, ATF_1504)
    str(result).should.match(r"src[\\/]atfu[\\/]standard_vectors[\\/]bc1504.xsvf$")


def test_find_vector_file_check_1508():
    result = find_vector_file(OP_CHECK, ATF_1508)
    str(result).should.match(r"src[\\/]atfu[\\/]standard_vectors[\\/]bc1508.xsvf$")


def test_find_vector_file_erase_1502():
    result = find_vector_file(OP_ERASE, ATF_1502)
    str(result).should.match(r"src[\\/]atfu[\\/]standard_vectors[\\/]e1502.xsvf$")


def test_find_vector_file_erase_1504():
    result = find_vector_file(OP_ERASE, ATF_1504)
    str(result).should.match(r"src[\\/]atfu[\\/]standard_vectors[\\/]e1504.xsvf$")


def test_find_vector_file_erase_1508():
    result = find_vector_file(OP_ERASE, ATF_1508)
    str(result).should.match(r"src[\\/]atfu[\\/]standard_vectors[\\/]e1508.xsvf$")


def test_atf_device_key_zero():
    atf_device_key.when.called_with(0).should.have.raised(ValueError)


def test_atf_device_key_string():
    atf_device_key.when.called_with("").should.have.raised(ValueError)


def test_atf_device_key_1500():
    atf_device_key.when.called_with(1500).should.have.raised(ValueError)


def test_atf_device_key_1502():
    atf_device_key.when.called_with(1502).should.return_value(ATF_1502)


def test_atf_device_key_1504():
    atf_device_key.when.called_with(1504).should.return_value(ATF_1504)


def test_atf_device_key_1508():
    atf_device_key.when.called_with(1508).should.return_value(ATF_1508)
