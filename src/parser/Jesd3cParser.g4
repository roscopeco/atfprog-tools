/*
 * JESD3C Parser for ANTLR4
 *
 * Copyright (c) 2024 Ross Bamford & Contributors
 * MIT License (see LICENSE.md)
 */

parser grammar Jesd3cParser;

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
 | user_data_field
 | device_id_field
 | default_test_cond_field
 | test_vector_field
 | pin_list_field
 ;

note_field
 : NOTE_ID note? TERMINATOR
 ;

note
 : NOTE
 ;

value_field
 : value_fuse_limit_field
 | value_pin_count_field
 | value_vec_limit_field
 ;

value_fuse_limit_field
 : VAL_FUS_ID fuse_limit TERMINATOR
 ;
 
fuse_limit
 : NUMBER
 | BINARY_NUMBER
 ;

value_pin_count_field
 : VAL_PIN_ID pin_count TERMINATOR
 ;

pin_count
 : NUMBER
 | BINARY_NUMBER
 ;
 
value_vec_limit_field
 : VAL_VEC_ID vec_limit TERMINATOR
 ;

vec_limit
 : NUMBER
 | BINARY_NUMBER
 ;

fuse_default_field
 : DEFAULT_ID value=BINARY_DIGIT TERMINATOR
 ;

fuse_list_field
 : FUSE_LIST_ID fuse_number fuse_data TERMINATOR
 ;

fuse_number
 : decimal
 ;

decimal
 : NUMBER
 | TEST_VEC_NUMBER
 | BINARY_NUMBER        /* yes, this is counter-intuitive, but here because */
 | BINARY_DIGIT         /* of numbers like 1001...  */
 ; 
 
fuse_data
 : BINARY_NUMBER BINARY_NUMBER*
 | BINARY_DIGIT
 ;

fuse_checksum_field
 : FUSE_CKSUM_ID fuse_cksum TERMINATOR
 ;

fuse_cksum
 : HEX_NUMBER
 ;
 
electrical_data_field
 : electrical_data_field_bin
 | electrical_data_field_hex
 ;

electrical_data_field_bin
 : ELEC_BIN_ID data=fuse_data TERMINATOR
 ;

electrical_data_field_hex
 : ELEC_HEX_ID data=hex_fuse_data TERMINATOR
 ;

hex_fuse_data
 : (HEX_NUMBER | NUMBER | BINARY_NUMBER) (HEX_NUMBER | NUMBER | BINARY_NUMBER)*
 | (HEX_DIGIT | BINARY_DIGIT)
 ;

user_data_field
 : user_data_field_bin
 | user_data_field_hex
 | user_data_field_asc
 ;

user_data_field_bin
 : USER_BIN_ID data=user_data_bin TERMINATOR
 ;

user_data_field_hex
 : USER_HEX_ID data=user_data_hex TERMINATOR
 ;

user_data_field_asc
 : USER_ASC_ID data=user_data_asc TERMINATOR
 ;

user_data_bin
 : BINARY_NUMBER BINARY_NUMBER*
 | BINARY_DIGIT
 ;

user_data_hex
 : (HEX_NUMBER | NUMBER | BINARY_NUMBER) (HEX_NUMBER | NUMBER | BINARY_NUMBER)*
 | (HEX_DIGIT | BINARY_DIGIT)
 ;

user_data_asc
 : NOTE
 ;

device_id_field
 : DEVICE_ID arch_code pinout_code TERMINATOR
 ;

arch_code
 : decimal
 ;

pinout_code
 : decimal
 ;

default_test_cond_field
 : DEF_TEST_COND_ID default_test_cond TERMINATOR
 ;

default_test_cond
 : BINARY_DIGIT
 ;

/* The embedded value field here is not to spec AFAICT, but observed in the wild... */
test_vector_field
 : TEST_VEC_ID vector_number (value_field)* test_cond? TERMINATOR
 ;

vector_number
 : decimal
 ;

test_cond
 : (TEST_COND | TEST_VEC_NUMBER) (TEST_COND | TEST_VEC_NUMBER)*
 ;

pin_list_field
 : PIN_LIST_ID pin_list? TERMINATOR
 ;

pin_list
 : pin_number+
 ;

pin_number
 : decimal
 ;

empty_field
 : TERMINATOR
 ;

xmit_cksum
 : HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
 ;

