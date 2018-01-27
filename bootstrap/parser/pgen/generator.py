import os
from string import Template
import pickle

from collection import CanonicalCollection
from set_generator import SetGenerator
from table import ParseTable

class ParserGenerator(object):
    def __init__(self, grammar, verbose=False):
        self.grammar = grammar
        self.table = ParseTable(CanonicalCollection(grammar), grammar, verbose=verbose)

    def generate(self, verbose=False):
        return dict(
            table=pickle.dumps(self.table.table),
            tokens=pickle.dumps(self.grammar.get_tokens()),
            productions=pickle.dumps(self.grammar.productions),
        )