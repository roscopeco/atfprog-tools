lexer grammar Jesd3cLexer;

STX         : '\u0002'                  -> pushMode(NOTE_MODE);
ETX         : '\u0003';
TERMINATOR  : '*';

NOTE_ID     : 'N' ('OTE')?              -> pushMode(NOTE_MODE);
VAL_FUS_ID  : 'QF';
VAL_PIN_ID  : 'QP';
VAL_VEC_ID  : 'QV';

FUSE_LIST_ID: 'L';

fragment
DIGIT       : [0-9];

fragment
BINARY_DIGIT
 : [0-1]
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

fragment
FIELD_CHARACTER
 : '\u0020'..'\u0029'
 | '\u002b'..'\u007e'
 ;

SPACE
 : [ \t\r\n] -> channel(HIDDEN)
 ;

mode NOTE_MODE;

NOTE        : FIELD_CHARACTER+;
NOTE_TERM   : '*'                       -> popMode, type(TERMINATOR);