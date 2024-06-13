import antlr4

import sure

from parser.Jesd3cParser import Jesd3cParser
from parser.Jesd3cLexer import Jesd3cLexer


def test_parse_empty_field():
    _, result = _test_empty_field("*")


def test_parse_note_field_basic_empty():
    _, result = _test_note_field("N*")

    result.note().should.be.none


def test_parse_note_field_basic_empty_with_space():
    _, result = _test_note_field("N *")

    result.note().getText().should.be.equal_to(" ")


def test_parse_note_field_basic_not_empty():
    _, result = _test_note_field("N some note *")

    result.note().getText().should.be.equal_to(" some note ")


def test_parse_note_field_basic_not_empty_multiline():
    _, result = _test_note_field("N some note\n some more note *")

    result.note().getText().should.be.equal_to(" some note some more note ")


def test_parse_note_field_long_id_empty():
    _, result = _test_note_field("NOTE*")

    result.note().should.be.none


def test_parse_note_field_long_id_empty_with_space():
    _, result = _test_note_field("NOTE *")

    result.note().getText().should.be.equal_to(" ")


def test_parse_note_field_long_id_not_empty():
    _, result = _test_note_field("NOTE some note *")

    result.note().getText().should.be.equal_to(" some note ")


def test_parse_value_fuse_limit_field():
    _, result = _test_value_fuse_limit_field("QF1024*")

    result.NUMBER().getText().should.be.equal_to("1024")


def test_parse_value_pin_count_field():
    _, result = _test_value_pin_count_field("QP44*")

    result.NUMBER().getText().should.be.equal_to("44")


def test_parse_value_vec_limit_field():
    _, result = _test_value_vec_limit_field("QV9001*")

    result.NUMBER().getText().should.be.equal_to("9001")


def test_parse_fuse_field_simple():
    _, result = _test_fuse_list_field("L0000 01010101*")

    result.fuse_number().NUMBER().should.be.none
    result.fuse_number().BINARY_NUMBER().should_not.be.none

    result.fuse_number().getText().should.be.equal_to("0000")
    result.fuse_data().getText().should.be.equal_to("01010101")


def test_parse_fuse_field_multiline_spaces():
    _, result = _test_fuse_list_field("L0001 01010101\n    11111111\n00000000\n*")

    result.fuse_number().NUMBER().should.be.none
    result.fuse_number().BINARY_NUMBER().should_not.be.none

    result.fuse_number().getText().should.be.equal_to("0001")
    result.fuse_data().getText().should.be.equal_to("010101011111111100000000")


def _test_empty_field(s: str):
    parser = _string_parser(s)

    result = parser.field()

    # Common tests
    result.empty_field().should_not.be.none
    result.note_field().should.be.none
    result.value_field().should.be.none
    result.fuse_list_field().should.be.none

    return parser, result.empty_field()


def _test_note_field(s: str):
    parser = _string_parser(s)

    result = parser.field()

    # Common tests
    result.empty_field().should.be.none
    result.note_field().should_not.be.none
    result.value_field().should.be.none
    result.fuse_list_field().should.be.none

    return parser, result.note_field()


def _test_value_field(s: str):
    parser = _string_parser(s)

    result = parser.field()

    # Common tests
    result.empty_field().should.be.none
    result.note_field().should.be.none
    result.value_field().should_not.be.none
    result.fuse_list_field().should.be.none

    return parser, result.value_field()


def _test_value_fuse_limit_field(s: str):
    parser, result = _test_value_field(s)

    result.value_fuse_limit_field().should_not.be.none
    result.value_pin_count_field().should.be.none
    result.value_vec_limit_field().should.be.none

    return parser, result.value_fuse_limit_field()


def _test_value_pin_count_field(s: str):
    parser, result = _test_value_field(s)

    result.value_fuse_limit_field().should.be.none
    result.value_pin_count_field().should_not.be.none
    result.value_vec_limit_field().should.be.none

    return parser, result.value_pin_count_field()


def _test_value_vec_limit_field(s: str):
    parser, result = _test_value_field(s)

    result.value_fuse_limit_field().should.be.none
    result.value_pin_count_field().should.be.none
    result.value_vec_limit_field().should_not.be.none

    return parser, result.value_vec_limit_field()


def _test_fuse_list_field(s: str):
    parser = _string_parser(s)

    result = parser.field()

    # Common tests
    result.empty_field().should.be.none
    result.note_field().should.be.none
    result.value_field().should.be.none
    result.fuse_list_field().should_not.be.none

    return parser, result.fuse_list_field()


def _string_lexer(s: str):
    return Jesd3cLexer(antlr4.InputStream(s))


def _string_parser(s: str):
    return Jesd3cParser(antlr4.CommonTokenStream(_string_lexer(s)))
