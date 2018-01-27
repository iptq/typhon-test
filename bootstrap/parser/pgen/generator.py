import os
from string import Template

from collection import CanonicalCollection
from set_generator import SetGenerator
from table import ParseTable

class ParserGenerator(object):
    def __init__(self, grammar, verbose=False):
        self.grammar = grammar
        self.table = ParseTable(CanonicalCollection(grammar), grammar, verbose=verbose)

    def generate(self):
        return dict(
            table=self.table.table,
            tokens=self.grammar.get_tokens(),
            productions=self.grammar.productions,
        )