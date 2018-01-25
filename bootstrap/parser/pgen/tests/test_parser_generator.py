import os
import sys
from io import StringIO
sys.path.append(os.path.realpath(os.path.dirname(os.path.dirname(__file__))))

from generator import ParserGenerator
from grammar import Grammar

def create_parser(grammar):
    output = StringIO()
    return ParserGenerator(grammar, output)

class TestParserGenerator(object):
    def test_parser_1(self):
        return
