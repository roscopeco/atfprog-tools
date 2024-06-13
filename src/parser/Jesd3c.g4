grammar Jesd3c;

options {
    tokenVocab = Jesd3cLexer; 
}

jes3dc
 : STX spec_field field* ETX xmit_cksum
 ;

spec_field
 : spec? TERMINATOR
 ;

spec
 : NOTE NOTE*
 ;

field
 : fuse_list_field
 | note_field
 | empty_field 
 ;

note_field
 : NOTE_ID note? TERMINATOR
 ;

note
 : NOTE NOTE*
 ;

fuse_list_field
 : FUSE_LIST_ID fuse_number fuse_data TERMINATOR
 ;

fuse_number
 : NUMBER
 | BINARY_NUMBER
 ;

fuse_data
 : BINARY_NUMBER BINARY_NUMBER*
 ;

empty_field
 : TERMINATOR
 ;

xmit_cksum
 : HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
 ;

