/*
 * JESD3C Parser for ANTLR4
 *
 * Copyright (c) 2024 Ross Bamford & Contributors
 * MIT License (see LICENSE.md)
 */

grammar Jesd3c;

options {
    tokenVocab = Jesd3cLexer; 
}

jesd3c
 : STX spec_field field* ETX xmit_cksum
 ;

spec_field
 : spec? TERMINATOR
 ;

spec
 : NOTE NOTE*
 ;

field
 : empty_field 
 | note_field
 | value_field
 | fuse_default_field
 | fuse_list_field
 | fuse_checksum_field
 | electrical_data_field
 ;

note_field
 : NOTE_ID note? TERMINATOR
 ;

note
 : NOTE NOTE*
 ;

value_field
 : value_fuse_limit_field
 | value_pin_count_field
 | value_vec_limit_field
 ;

value_fuse_limit_field
 : VAL_FUS_ID NUMBER TERMINATOR
 ;

value_pin_count_field
 : VAL_PIN_ID NUMBER TERMINATOR
 ;

value_vec_limit_field
 : VAL_VEC_ID NUMBER TERMINATOR
 ;

fuse_default_field
 : DEFAULT_ID BINARY_DIGIT TERMINATOR
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
 | BINARY_DIGIT
 ;

fuse_checksum_field
 : FUSE_CKSUM_ID xmit_cksum TERMINATOR
 ;

electrical_data_field
 : electrical_data_field_bin
 | electrical_data_field_hex
 ;

electrical_data_field_bin
 : ELEC_BIN_ID fuse_data TERMINATOR
 ;

electrical_data_field_hex
 : ELEC_HEX_ID hex_fuse_data TERMINATOR
 ;

hex_fuse_data
 : (HEX_NUMBER | NUMBER | BINARY_NUMBER) (HEX_NUMBER | NUMBER | BINARY_NUMBER)*
 | HEX_DIGIT
 ;

empty_field
 : TERMINATOR
 ;

xmit_cksum
 : HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
 ;

