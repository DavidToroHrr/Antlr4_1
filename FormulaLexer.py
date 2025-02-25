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
        4,0,11,97,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,1,1,1,1,2,1,2,
        1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,76,8,
        8,1,9,4,9,79,8,9,11,9,12,9,80,1,9,1,9,4,9,85,8,9,11,9,12,9,86,3,
        9,89,8,9,1,10,4,10,92,8,10,11,10,12,10,93,1,10,1,10,0,0,11,1,1,3,
        2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,1,0,2,1,0,48,57,3,
        0,9,10,13,13,32,32,103,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,
        0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,
        0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,1,23,1,0,0,0,3,25,1,0,0,0,5,27,1,
        0,0,0,7,29,1,0,0,0,9,31,1,0,0,0,11,33,1,0,0,0,13,35,1,0,0,0,15,37,
        1,0,0,0,17,75,1,0,0,0,19,78,1,0,0,0,21,91,1,0,0,0,23,24,5,42,0,0,
        24,2,1,0,0,0,25,26,5,47,0,0,26,4,1,0,0,0,27,28,5,37,0,0,28,6,1,0,
        0,0,29,30,5,43,0,0,30,8,1,0,0,0,31,32,5,45,0,0,32,10,1,0,0,0,33,
        34,5,40,0,0,34,12,1,0,0,0,35,36,5,41,0,0,36,14,1,0,0,0,37,38,5,44,
        0,0,38,16,1,0,0,0,39,40,5,115,0,0,40,41,5,117,0,0,41,42,5,109,0,
        0,42,76,5,97,0,0,43,44,5,112,0,0,44,45,5,114,0,0,45,46,5,111,0,0,
        46,47,5,109,0,0,47,48,5,101,0,0,48,49,5,100,0,0,49,50,5,105,0,0,
        50,76,5,111,0,0,51,52,5,100,0,0,52,53,5,101,0,0,53,54,5,115,0,0,
        54,55,5,118,0,0,55,56,5,105,0,0,56,57,5,97,0,0,57,58,5,99,0,0,58,
        59,5,105,0,0,59,60,5,111,0,0,60,76,5,110,0,0,61,62,5,109,0,0,62,
        63,5,101,0,0,63,64,5,100,0,0,64,65,5,105,0,0,65,66,5,97,0,0,66,67,
        5,80,0,0,67,68,5,111,0,0,68,69,5,110,0,0,69,70,5,100,0,0,70,71,5,
        101,0,0,71,72,5,114,0,0,72,73,5,97,0,0,73,74,5,100,0,0,74,76,5,97,
        0,0,75,39,1,0,0,0,75,43,1,0,0,0,75,51,1,0,0,0,75,61,1,0,0,0,76,18,
        1,0,0,0,77,79,7,0,0,0,78,77,1,0,0,0,79,80,1,0,0,0,80,78,1,0,0,0,
        80,81,1,0,0,0,81,88,1,0,0,0,82,84,5,46,0,0,83,85,7,0,0,0,84,83,1,
        0,0,0,85,86,1,0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,89,1,0,0,0,88,
        82,1,0,0,0,88,89,1,0,0,0,89,20,1,0,0,0,90,92,7,1,0,0,91,90,1,0,0,
        0,92,93,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,95,1,0,0,0,95,96,
        6,10,0,0,96,22,1,0,0,0,6,0,75,80,86,88,93,1,6,0,0
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
    WS = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'*'", "'/'", "'%'", "'+'", "'-'", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>",
            "ID", "NUMBER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "ID", "NUMBER", "WS" ]

    grammarFileName = "Formula.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


