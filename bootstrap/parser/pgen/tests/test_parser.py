import os
import sys
sys.path.insert(0, os.path.realpath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

from lexer import Lexer
from pgen.grammar import Grammar
from pgen.generator import ParserGenerator
from pgen.parser import Parser

class TestParser(object):
    def test_balanced_parentheses_parser(self):
        data = "B = EMPTY, B + '(' + B + ')'"
        source = "()"
        pgen = ParserGenerator(Grammar.from_data(data), verbose=True)
        lexer = Lexer(source)
        parser = Parser(pgen.generate())
        result = parser.parse(lexer, verbose=True)
        print("result", result)
        assert 0
