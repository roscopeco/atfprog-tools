import antlr4

import sure

from parser.Jesd3cParser import Jesd3cParser
from parser.Jesd3cLexer import Jesd3cLexer

import test.atfu.test_cases

from importlib.resources import files

from antlr4.error.ErrorStrategy import BailErrorStrategy


def test_parse_empty_jed():
    parser = _string_parser(
        """\x02Version 4.45.1*
        \x030000
        """
    )

    result = parser.jesd3c()

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

    result = parser.jesd3c()

    result.spec_field().should_not.be.none
    result.spec_field().spec().should_not.be.none

    result.spec_field().spec().getText().should.be.equal_to(
        "Version 4.45.1\n        JEDEC file for: ATF1504 PLCC44\n        Created on: Wed Jun 12 14:18:48 2024\n\n        "
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

    result = parser.jesd3c()

    result.spec_field().should_not.be.none
    result.spec_field().spec().should_not.be.none

    result.spec_field().spec().getText().should.be.equal_to("Version 4.45.1")

    result.field().should.be.empty

    result.xmit_cksum().should_not.be.none
    result.xmit_cksum().getText().should.be.equal_to("1234")


def test_bug3():
    jed = load_testcase("bug3.jed")
    parser = _string_parser(jed)

    result = parser.jesd3c()

    result.spec_field().should_not.be.none
    result.spec_field().spec().should_not.be.none

    result.spec_field().spec().getText().should.be.equal_to(
        "JEDEC file for: ATF1508AS\nCreated on: Mon May 20 15:20:33 2024\n"
    )

    result.field().should_not.be.empty
    # TODO assert against the fields!

    result.xmit_cksum().should_not.be.none
    result.xmit_cksum().getText().should.be.equal_to("7A3A")


def test_bug4():
    jed = load_testcase("bug3.jed")
    parser = _string_parser(jed)

    result = parser.jesd3c()

    result.spec_field().should_not.be.none
    result.spec_field().spec().should_not.be.none

    result.spec_field().spec().getText().should.be.equal_to(
        "JEDEC file for: ATF1508AS\nCreated on: Mon May 20 15:20:33 2024\n"
    )

    result.field().should_not.be.empty
    # TODO assert against the fields!

    result.xmit_cksum().should_not.be.none
    result.xmit_cksum().getText().should.be.equal_to("7A3A")


def load_testcase(name: str) -> str:
    with open(files("test.atfu.test_cases.jed").joinpath(name)) as f:
        return f.read()


def _string_lexer(s: str):
    lexer = Jesd3cLexer(antlr4.InputStream(s))
    lexer._errHandler = BailErrorStrategy()
    return lexer


def _string_parser(s: str):
    parser = Jesd3cParser(antlr4.CommonTokenStream(_string_lexer(s)))
    parser._errHandler = BailErrorStrategy()
    return parser
