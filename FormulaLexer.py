# Generated from Formula.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,12,73,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,1,1,
        1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,5,8,44,
        8,8,10,8,12,8,47,9,8,1,9,4,9,50,8,9,11,9,12,9,51,1,9,1,9,4,9,56,
        8,9,11,9,12,9,57,3,9,60,8,9,1,10,3,10,63,8,10,1,10,1,10,1,11,4,11,
        68,8,11,11,11,12,11,69,1,11,1,11,0,0,12,1,1,3,2,5,3,7,4,9,5,11,6,
        13,7,15,8,17,9,19,10,21,11,23,12,1,0,4,3,0,65,90,95,95,97,122,4,
        0,48,57,65,90,95,95,97,122,1,0,48,57,3,0,9,9,13,13,32,32,78,0,1,
        1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,
        0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,
        0,0,0,23,1,0,0,0,1,25,1,0,0,0,3,27,1,0,0,0,5,29,1,0,0,0,7,31,1,0,
        0,0,9,33,1,0,0,0,11,35,1,0,0,0,13,37,1,0,0,0,15,39,1,0,0,0,17,41,
        1,0,0,0,19,49,1,0,0,0,21,62,1,0,0,0,23,67,1,0,0,0,25,26,5,42,0,0,
        26,2,1,0,0,0,27,28,5,47,0,0,28,4,1,0,0,0,29,30,5,37,0,0,30,6,1,0,
        0,0,31,32,5,43,0,0,32,8,1,0,0,0,33,34,5,45,0,0,34,10,1,0,0,0,35,
        36,5,40,0,0,36,12,1,0,0,0,37,38,5,41,0,0,38,14,1,0,0,0,39,40,5,44,
        0,0,40,16,1,0,0,0,41,45,7,0,0,0,42,44,7,1,0,0,43,42,1,0,0,0,44,47,
        1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,18,1,0,0,0,47,45,1,0,0,0,
        48,50,7,2,0,0,49,48,1,0,0,0,50,51,1,0,0,0,51,49,1,0,0,0,51,52,1,
        0,0,0,52,59,1,0,0,0,53,55,5,46,0,0,54,56,7,2,0,0,55,54,1,0,0,0,56,
        57,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,58,60,1,0,0,0,59,53,1,0,0,
        0,59,60,1,0,0,0,60,20,1,0,0,0,61,63,5,13,0,0,62,61,1,0,0,0,62,63,
        1,0,0,0,63,64,1,0,0,0,64,65,5,10,0,0,65,22,1,0,0,0,66,68,7,3,0,0,
        67,66,1,0,0,0,68,69,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,71,1,
        0,0,0,71,72,6,11,0,0,72,24,1,0,0,0,7,0,45,51,57,59,62,69,1,6,0,0
    ]

class FormulaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    ID = 9
    NUMBER = 10
    NEWLINE = 11
    WS = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'*'", "'/'", "'%'", "'+'", "'-'", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>",
            "ID", "NUMBER", "NEWLINE", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "ID", "NUMBER", "NEWLINE", "WS" ]

    grammarFileName = "Formula.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


