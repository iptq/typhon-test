import sys
import os
sys.path.append(os.path.realpath(os.path.dirname(__file__)))

import ast
from functools import reduce
from operator import xor

from orderedset import OrderedSet
from .util import flatten
from .production import Production
from grammar.symbols import *

class Rule(object):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    @property
    def pair(self):
        return self.left, self.right

class Grammar(object):
    def __init__(self, productions, start, verbose=False):
        keys = list(map(lambda r: r.left, productions))
        assert start in keys
        
        self._terminals = None
        self._tokens = None

        self.nonterminals = keys
        self.start = GNT(start)

        self.augmented = Production(0, "$accept", [self.start], 0, self)
        self.augmented.augmented = True
        self.productions = [self.augmented]
        for rule in productions:
            nonterminal, rules = rule.pair
            for i, production in enumerate(rules):
                obj = Production(i, nonterminal, production, len(self.productions), self)
                self.productions.append(obj)

        self._productions_for_symbol = dict()
        self._productions_with_symbol = dict()

    @staticmethod
    def from_file(grammar_file, verbose=False):
        with open(grammar_file, "r") as f:
            data = f.read()
        return Grammar.from_data(data, verbose=verbose)

    @staticmethod
    def from_data(data, verbose=False):
        rules = OrderedSet()
        productions = ast.parse(data).body
        nonterminals = [production.targets[0].id for production in productions]

        for production in productions:
            rule = Rule(production.targets[0].id, flatten(production.value, nonterminals))
            rules.add(rule)

        return Grammar(rules, productions[0].targets[0].id, verbose=verbose)

    @property
    def terminals(self):
        if not self._terminals:
            self._terminals = OrderedSet()
            for production in self.productions:
                for symbol in production.right:
                    assert isinstance(symbol, GrammarSymbol)
                    if symbol.terminal:
                        self._terminals.add(symbol)
        return self._terminals

    @property
    def tokens(self):
        if not self._tokens:
            self._tokens = OrderedSet()
            for production in self.productions:
                for symbol in production.right:
                    assert isinstance(symbol, GrammarSymbol)
                    if not symbol.terminal and symbol.key not in self.nonterminals:
                        self._tokens.add(symbol)
        return self._tokens

    def get_tokens(self):
        return dict()

    def is_token(self, symbol):
        return symbol in self.terminals or symbol in self.tokens
    
    def print(self):
        print("Grammar:")
        for production in self.productions:
            print("{}: {}".format(str(production.number).rjust(3), repr(production)))
        print("---")

    def productions_for_symbol(self, symbol):
        if symbol.key not in self._productions_for_symbol:
            self._productions_for_symbol[symbol.key] = OrderedSet([p for p in self.productions if p.left == symbol.key])
        return self._productions_for_symbol.get(symbol.key)

    def productions_with_symbol(self, symbol):
        if symbol.key not in self._productions_with_symbol:
            self._productions_with_symbol[symbol.key] = OrderedSet([p for p in self.productions if symbol in p.right_set])
        return self._productions_with_symbol.get(symbol.key)
