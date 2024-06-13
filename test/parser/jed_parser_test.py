import antlr4

import sure

from parser.Jesd3cParser import Jesd3cParser
from parser.Jesd3cLexer import Jesd3cLexer


def test_parse_empty_jed():
    parser = _string_parser(
        """\x02Version 4.45.1*
        \x030000
        """
    )

    result = parser.jes3dc()

    result.spec_field().should_not.be.none
    result.spec_field().spec().should_not.be.none

    result.spec_field().spec().getText().should.be.equal_to("Version 4.45.1")

    result.field().should.be.empty

    result.xmit_cksum().should_not.be.none
    result.xmit_cksum().getText().should.be.equal_to("0000")


def test_parse_empty_jed_multiline_spec():
    parser = _string_parser(
        """\x02Version 4.45.1
        JEDEC file for: ATF1504 PLCC44
        Created on: Wed Jun 12 14:18:48 2024

        *
        \x030000
        """
    )

    result = parser.jes3dc()

    result.spec_field().should_not.be.none
    result.spec_field().spec().should_not.be.none

    result.spec_field().spec().getText().should.be.equal_to(
        "Version 4.45.1        JEDEC file for: ATF1504 PLCC44        Created on: Wed Jun 12 14:18:48 2024        "
    )

    result.field().should.be.empty

    result.xmit_cksum().should_not.be.none
    result.xmit_cksum().getText().should.be.equal_to("0000")


def test_parse_jed_with_checksum():
    parser = _string_parser(
        """\x02Version 4.45.1*
        \x031234
        """
    )

    result = parser.jes3dc()

    result.spec_field().should_not.be.none
    result.spec_field().spec().should_not.be.none

    result.spec_field().spec().getText().should.be.equal_to("Version 4.45.1")

    result.field().should.be.empty

    result.xmit_cksum().should_not.be.none
    result.xmit_cksum().getText().should.be.equal_to("1234")


def _string_lexer(s: str):
    return Jesd3cLexer(antlr4.InputStream(s))


def _string_parser(s: str):
    return Jesd3cParser(antlr4.CommonTokenStream(_string_lexer(s)))
