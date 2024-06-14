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

/* Note mode, just grabs text until terminator */
mode NOTE_MODE;

/* This could be ~'*' but the below makes it easier to see 
   where in the spec it comes from... */
fragment
FIELD_CHARACTER
 : '\u0020'..'\u0029'
 | '\u002b'..'\u007e'
 ;

NOTE        : FIELD_CHARACTER+;
NOTE_TERM   : '*'                       -> popMode, type(TERMINATOR);