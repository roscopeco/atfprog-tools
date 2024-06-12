lexer grammar Jesd3cLexer;

STX         : '\u0002';
ETX         : '\u0003';
TERMINATOR  : '*';

NOTE_ID     : 'N' ('OTE')?              -> pushMode(NOTE_MODE);
FUSE_LIST_ID: 'L';

DIGIT       : [0-9];

HEX_DIGIT
 : DIGIT | [A-F]
 ;

BINARY_DIGIT
 : [0-1]
 ;

BINARY_NUMBER
 : BINARY_DIGIT BINARY_DIGIT*
 ;

NUMBER
 : DIGIT DIGIT*
 ;

SPACE
 : [ \t\r\n] -> channel(HIDDEN)
 ;

mode NOTE_MODE;

NOTE        : ~('*')+;
NOTE_TERM   : '*'                       -> popMode;