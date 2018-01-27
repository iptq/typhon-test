import os
import sys
sys.path.insert(0, os.path.realpath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

from lexer import Lexer
from pgen.grammar import Grammar
from pgen.grammar.symbols import *
from pgen.generator import ParserGenerator
from pgen.parser import Parser

class TestParser(object):
    def test_balanced_parentheses_parser(self):
        data = "B = EMPTY, B + '(' + B + ')'"
        pgen = ParserGenerator(Grammar.from_data(data))
        parser = Parser(pgen.generate())

        lexer = Lexer("()")
        result = parser.parse(lexer)
        assert result == GNT("B")
        assert result.children == [GLiteral("("), GLiteral(")")]

        lexer = Lexer("(())")
        result = parser.parse(lexer)
        assert result == GNT("B")
        assert result.children == [GLiteral("("), GNT("B"), GLiteral(")")]
        assert result.children[1].children == [GLiteral("("), GLiteral(")")]

        lexer = Lexer("(())()")
        result = parser.parse(lexer)
        assert result == GNT("B")
        assert result.children == [GNT("B"), GLiteral("("), GLiteral(")")]
        assert result.children[0].children == [GLiteral("("), GNT("B"), GLiteral(")")]
        assert result.children[0].children[1].children == [GLiteral("("), GLiteral(")")]
