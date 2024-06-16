/*
 * JESD3C Lexer for ANTLR4
 *
 * Copyright (c) 2024 Ross Bamford & Contributors
 * MIT License (see LICENSE.md)
 */
lexer grammar Jesd3cLexer;

STX             : '\u0002'                  -> pushMode(NOTE_MODE);     /* spec field is a NOTE with no identifier */
ETX             : '\u0003';
TERMINATOR      : '*';

NOTE_ID         : 'N' ('OTE')?              -> pushMode(NOTE_MODE);     /* Regular note field, just grab text until terminator */

VAL_FUS_ID      : 'QF'                      -> pushMode(VALUE_MODE);
VAL_PIN_ID      : 'QP'                      -> pushMode(VALUE_MODE);
VAL_VEC_ID      : 'QV'                      -> pushMode(VALUE_MODE);

DEFAULT_ID      : 'F'                       -> pushMode(VALUE_MODE);

FUSE_LIST_ID    : 'L'                       -> pushMode(VALUE_MODE);

FUSE_CKSUM_ID   : 'C'                       -> pushMode(VALUE_MODE);

ELEC_HEX_ID     : 'EH'                      -> pushMode(VALUE_MODE);
ELEC_BIN_ID     : 'E'                       -> pushMode(VALUE_MODE);

USER_ASC_ID     : 'UA'                      -> pushMode(NOTE_MODE);
USER_HEX_ID     : 'UH'                      -> pushMode(VALUE_MODE);
USER_BIN_ID     : 'U'                       -> pushMode(VALUE_MODE);

DEVICE_ID       : 'J'                       -> pushMode(VALUE_MODE);

DEF_TEST_COND_ID: 'X'                       -> pushMode(VALUE_MODE);
TEST_VEC_ID     : 'V'                       -> pushMode(TEST_VEC_MODE);

PIN_LIST_ID     : 'P'                       -> pushMode(VALUE_MODE);

HEX_DIGIT
 : DIGIT | [A-F]
 ;

SPACE
 : [ \t\r\n] -> channel(HIDDEN)
 ;

mode VALUE_MODE;

BINARY_DIGIT
 : [0-1]
 ;

fragment
DIGIT
 : BINARY_DIGIT | [2-9]
 ;

BINARY_NUMBER
 : BINARY_DIGIT BINARY_DIGIT*
 ;

NUMBER
 : DIGIT DIGIT*
 ;

HEX_NUMBER
 : HEX_DIGIT HEX_DIGIT*
 ;

VALUE_TERM   : '*'                      -> popMode, type(TERMINATOR);

VALUE_SPACE
 : [ \t\r\n]                            -> channel(HIDDEN), type(SPACE)
 ;

mode TEST_VEC_MODE;

fragment
TEST_DIGIT
 : [0-9]
 ;

TEST_VEC_NUMBER
 : TEST_DIGIT TEST_DIGIT*
 ;

TEST_COND   : (TEST_DIGIT | 'B' | 'C' | 'D' | 'F' | 'H' | 'K' | 'L' | 'N' | 'P' | 'R' | 'T' | 'U' | 'X' | 'Z')+;

/* 
 * These are weird, and not strictly to spec - but CSIM will sometimes embed values 
 * inside test vectors for some reason.... 🤷
 */
WEIRD_VAL_FUS_ID      : 'QF'              -> pushMode(VALUE_MODE), type(VAL_FUS_ID);
WEIRD_VAL_PIN_ID      : 'QP'              -> pushMode(VALUE_MODE), type(VAL_PIN_ID);
WEIRD_VAL_VEC_ID      : 'QV'              -> pushMode(VALUE_MODE), type(VAL_VEC_ID);

TEST_TERM   : '*'                       -> popMode, type(TERMINATOR);

TEST_SPACE
 : [ \t\r\n]                            -> channel(HIDDEN), type(SPACE)
 ;

/* Note mode, just grabs text until terminator */
mode NOTE_MODE;

/* 
 * Not _exactly_ to spec - only printable characters other than '*'
 * are defined there, but this represents what we actually want 
 * (including whitespace etc)...
 */
fragment
FIELD_CHARACTER : ~'*';

NOTE            : FIELD_CHARACTER+;
NOTE_TERM       : '*'                       -> popMode, type(TERMINATOR);