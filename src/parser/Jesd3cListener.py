# Generated from src/parser/Jesd3c.g4 by ANTLR 4.13.1
from antlr4 import *

if "." in __name__:
    from .Jesd3cParser import Jesd3cParser
else:
    from Jesd3cParser import Jesd3cParser


# This class defines a complete listener for a parse tree produced by Jesd3cParser.
class Jesd3cListener(ParseTreeListener):
    # Enter a parse tree produced by Jesd3cParser#jes3dc.
    def enterJes3dc(self, ctx: Jesd3cParser.Jes3dcContext):
        pass

    # Exit a parse tree produced by Jesd3cParser#jes3dc.
    def exitJes3dc(self, ctx: Jesd3cParser.Jes3dcContext):
        pass

    # Enter a parse tree produced by Jesd3cParser#spec_field.
    def enterSpec_field(self, ctx: Jesd3cParser.Spec_fieldContext):
        pass

    # Exit a parse tree produced by Jesd3cParser#spec_field.
    def exitSpec_field(self, ctx: Jesd3cParser.Spec_fieldContext):
        pass

    # Enter a parse tree produced by Jesd3cParser#spec.
    def enterSpec(self, ctx: Jesd3cParser.SpecContext):
        pass

    # Exit a parse tree produced by Jesd3cParser#spec.
    def exitSpec(self, ctx: Jesd3cParser.SpecContext):
        pass

    # Enter a parse tree produced by Jesd3cParser#field.
    def enterField(self, ctx: Jesd3cParser.FieldContext):
        pass

    # Exit a parse tree produced by Jesd3cParser#field.
    def exitField(self, ctx: Jesd3cParser.FieldContext):
        pass

    # Enter a parse tree produced by Jesd3cParser#note_field.
    def enterNote_field(self, ctx: Jesd3cParser.Note_fieldContext):
        pass

    # Exit a parse tree produced by Jesd3cParser#note_field.
    def exitNote_field(self, ctx: Jesd3cParser.Note_fieldContext):
        pass

    # Enter a parse tree produced by Jesd3cParser#note.
    def enterNote(self, ctx: Jesd3cParser.NoteContext):
        pass

    # Exit a parse tree produced by Jesd3cParser#note.
    def exitNote(self, ctx: Jesd3cParser.NoteContext):
        pass

    # Enter a parse tree produced by Jesd3cParser#fuse_list_field.
    def enterFuse_list_field(self, ctx: Jesd3cParser.Fuse_list_fieldContext):
        pass

    # Exit a parse tree produced by Jesd3cParser#fuse_list_field.
    def exitFuse_list_field(self, ctx: Jesd3cParser.Fuse_list_fieldContext):
        pass

    # Enter a parse tree produced by Jesd3cParser#fuse_number.
    def enterFuse_number(self, ctx: Jesd3cParser.Fuse_numberContext):
        pass

    # Exit a parse tree produced by Jesd3cParser#fuse_number.
    def exitFuse_number(self, ctx: Jesd3cParser.Fuse_numberContext):
        pass

    # Enter a parse tree produced by Jesd3cParser#fuse_data.
    def enterFuse_data(self, ctx: Jesd3cParser.Fuse_dataContext):
        pass

    # Exit a parse tree produced by Jesd3cParser#fuse_data.
    def exitFuse_data(self, ctx: Jesd3cParser.Fuse_dataContext):
        pass

    # Enter a parse tree produced by Jesd3cParser#empty_field.
    def enterEmpty_field(self, ctx: Jesd3cParser.Empty_fieldContext):
        pass

    # Exit a parse tree produced by Jesd3cParser#empty_field.
    def exitEmpty_field(self, ctx: Jesd3cParser.Empty_fieldContext):
        pass

    # Enter a parse tree produced by Jesd3cParser#xmit_cksum.
    def enterXmit_cksum(self, ctx: Jesd3cParser.Xmit_cksumContext):
        pass

    # Exit a parse tree produced by Jesd3cParser#xmit_cksum.
    def exitXmit_cksum(self, ctx: Jesd3cParser.Xmit_cksumContext):
        pass


del Jesd3cParser
