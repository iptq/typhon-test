from io import StringIO

from parser.grammar import Grammar
from parser.parse import ParserGenerator


def create_parser(grammar):
    output = StringIO()
    return ParserGenerator(grammar, output)


class TestParserGenerator(object):
    def test_parser_1(self):
        return
