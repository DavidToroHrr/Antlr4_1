# Generated from Formula.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .FormulaParser import FormulaParser
else:
    from FormulaParser import FormulaParser

# This class defines a complete generic visitor for a parse tree produced by FormulaParser.

class FormulaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FormulaParser#file.
    def visitFile(self, ctx:FormulaParser.FileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#formula.
    def visitFormula(self, ctx:FormulaParser.FormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#MulDivMod.
    def visitMulDivMod(self, ctx:FormulaParser.MulDivModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#Number.
    def visitNumber(self, ctx:FormulaParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#AddSub.
    def visitAddSub(self, ctx:FormulaParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#Parens.
    def visitParens(self, ctx:FormulaParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#FunctionCall.
    def visitFunctionCall(self, ctx:FormulaParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#ColumnReference.
    def visitColumnReference(self, ctx:FormulaParser.ColumnReferenceContext):
        return self.visitChildren(ctx)



del FormulaParser