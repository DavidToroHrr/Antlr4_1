# Generated from Formula.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,12,53,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,0,
        1,0,1,1,1,1,5,1,16,8,1,10,1,12,1,19,9,1,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,5,2,32,8,2,10,2,12,2,35,9,2,1,2,1,2,1,2,3,2,
        40,8,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,48,8,2,10,2,12,2,51,9,2,1,2,0,
        1,4,3,0,2,4,0,2,1,0,1,3,1,0,4,5,57,0,7,1,0,0,0,2,13,1,0,0,0,4,39,
        1,0,0,0,6,8,3,2,1,0,7,6,1,0,0,0,8,9,1,0,0,0,9,7,1,0,0,0,9,10,1,0,
        0,0,10,11,1,0,0,0,11,12,5,0,0,1,12,1,1,0,0,0,13,17,3,4,2,0,14,16,
        5,11,0,0,15,14,1,0,0,0,16,19,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,
        18,3,1,0,0,0,19,17,1,0,0,0,20,21,6,2,-1,0,21,22,5,6,0,0,22,23,3,
        4,2,0,23,24,5,7,0,0,24,40,1,0,0,0,25,40,5,10,0,0,26,27,5,9,0,0,27,
        28,5,6,0,0,28,33,3,4,2,0,29,30,5,8,0,0,30,32,3,4,2,0,31,29,1,0,0,
        0,32,35,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,36,1,0,0,0,35,33,
        1,0,0,0,36,37,5,7,0,0,37,40,1,0,0,0,38,40,5,9,0,0,39,20,1,0,0,0,
        39,25,1,0,0,0,39,26,1,0,0,0,39,38,1,0,0,0,40,49,1,0,0,0,41,42,10,
        6,0,0,42,43,7,0,0,0,43,48,3,4,2,7,44,45,10,5,0,0,45,46,7,1,0,0,46,
        48,3,4,2,6,47,41,1,0,0,0,47,44,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,
        0,49,50,1,0,0,0,50,5,1,0,0,0,51,49,1,0,0,0,6,9,17,33,39,47,49
    ]

class FormulaParser ( Parser ):

    grammarFileName = "Formula.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "'/'", "'%'", "'+'", "'-'", "'('", 
                     "')'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "NUMBER", "NEWLINE", "WS" ]

    RULE_file = 0
    RULE_formula = 1
    RULE_expression = 2

    ruleNames =  [ "file", "formula", "expression" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    ID=9
    NUMBER=10
    NEWLINE=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(FormulaParser.EOF, 0)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FormulaParser.FormulaContext)
            else:
                return self.getTypedRuleContext(FormulaParser.FormulaContext,i)


        def getRuleIndex(self):
            return FormulaParser.RULE_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFile" ):
                listener.enterFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFile" ):
                listener.exitFile(self)




    def file_(self):

        localctx = FormulaParser.FileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_file)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.formula()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1600) != 0)):
                    break

            self.state = 11
            self.match(FormulaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(FormulaParser.ExpressionContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(FormulaParser.NEWLINE)
            else:
                return self.getToken(FormulaParser.NEWLINE, i)

        def getRuleIndex(self):
            return FormulaParser.RULE_formula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormula" ):
                listener.enterFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormula" ):
                listener.exitFormula(self)




    def formula(self):

        localctx = FormulaParser.FormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_formula)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.expression(0)
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 14
                self.match(FormulaParser.NEWLINE)
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FormulaParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MulDivModContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormulaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FormulaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FormulaParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivMod" ):
                listener.enterMulDivMod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivMod" ):
                listener.exitMulDivMod(self)


    class NumberContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormulaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(FormulaParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)


    class AddSubContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormulaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FormulaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FormulaParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)


    class ParensContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormulaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(FormulaParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)


    class FunctionCallContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormulaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(FormulaParser.ID, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FormulaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FormulaParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)


    class ColumnReferenceContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormulaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(FormulaParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnReference" ):
                listener.enterColumnReference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnReference" ):
                listener.exitColumnReference(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = FormulaParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = FormulaParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 21
                self.match(FormulaParser.T__5)
                self.state = 22
                self.expression(0)
                self.state = 23
                self.match(FormulaParser.T__6)
                pass

            elif la_ == 2:
                localctx = FormulaParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 25
                self.match(FormulaParser.NUMBER)
                pass

            elif la_ == 3:
                localctx = FormulaParser.FunctionCallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 26
                self.match(FormulaParser.ID)
                self.state = 27
                self.match(FormulaParser.T__5)
                self.state = 28
                self.expression(0)
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==8:
                    self.state = 29
                    self.match(FormulaParser.T__7)
                    self.state = 30
                    self.expression(0)
                    self.state = 35
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 36
                self.match(FormulaParser.T__6)
                pass

            elif la_ == 4:
                localctx = FormulaParser.ColumnReferenceContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 38
                self.match(FormulaParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 49
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 47
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = FormulaParser.MulDivModContext(self, FormulaParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 41
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 42
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 43
                        self.expression(7)
                        pass

                    elif la_ == 2:
                        localctx = FormulaParser.AddSubContext(self, FormulaParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 44
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 45
                        _la = self._input.LA(1)
                        if not(_la==4 or _la==5):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 46
                        self.expression(6)
                        pass

             
                self.state = 51
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         




