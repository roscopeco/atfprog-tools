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

VAL_FUS_ID      : 'QF';
VAL_PIN_ID      : 'QP';
VAL_VEC_ID      : 'QV';

DEFAULT_ID      : 'F';

FUSE_LIST_ID    : 'L';

FUSE_CKSUM_ID   : 'C';

BINARY_DIGIT
 : [0-1]
 ;

fragment
DIGIT       
 : BINARY_DIGIT | [2-9]
 ;

HEX_DIGIT
 : DIGIT | [A-F]
 ;

BINARY_NUMBER
 : BINARY_DIGIT BINARY_DIGIT*
 ;

NUMBER
 : DIGIT DIGIT*
 ;

/* This could be ~'*' but the below makes it easier to see 
   where in the spec it comes from... */
fragment
FIELD_CHARACTER
 : '\u0020'..'\u0029'
 | '\u002b'..'\u007e'
 ;

SPACE
 : [ \t\r\n] -> channel(HIDDEN)
 ;


/* Note mode, just grabs text until terminator */
mode NOTE_MODE;

NOTE        : FIELD_CHARACTER+;
NOTE_TERM   : '*'                       -> popMode, type(TERMINATOR);