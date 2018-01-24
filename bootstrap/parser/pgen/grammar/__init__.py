import ast
from copy import deepcopy
from functools import reduce
from operator import xor

from orderedset import OrderedSet
from .production import Production
from .symbols import *

def flatten(node, nonterminals):
    def rec_flatten(items, front):
        current = []
        for node in items:
            if isinstance(node, ast.BinOp):
                if isinstance(node.op, ast.Add):
                    left = rec_flatten([node.left], deepcopy(front))
                    right = rec_flatten([node.right], deepcopy(front))
                    for sym1 in left:
                        for sym2 in right:
                            full = deepcopy(front)
                            full.extend(sym1 + sym2)
                            current.append(full)
            elif isinstance(node, ast.Name):
                obj = None
                if node.id == "IDENT":
                    obj = GIdent()
                elif node.id == "NUMBER":
                    obj = GNum()
                elif node.id == "STRING":
                    obj = GStr()
                elif node.id == "NEWLINE":
                    obj = GNEWLINE()
                elif node.id in nonterminals:
                    obj = GNT(node.id)
                front.append(obj)
                current.append(deepcopy(front))
            elif isinstance(node, ast.Str):
                front.append(GLiteral(node.s))
                current.append(deepcopy(front))
            elif isinstance(node, ast.Tuple):
                for element in node.elts:
                    flat = rec_flatten([element], deepcopy(front))
                    for sym in flat:
                        current.append(sym)
            else:
                raise NotImplementedError(type(node))
            return current
    return rec_flatten([node], [])

class Rule(object):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    @property
    def pair(self):
        return self.left, self.right
    

class Grammar(object):
    def __init__(self, productions, start):
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
                self.productions.append(Production(i, nonterminal, production, len(self.productions), self))

        self._productions_for_symbol = dict()
        self._productions_with_symbol = dict()

    @staticmethod
    def from_file(grammar_file):
        with open(grammar_file, "r") as f:
            data = f.read()
        return Grammar.from_data(data)

    @staticmethod
    def from_data(data):
        rules = OrderedSet()
        productions = ast.parse(data).body
        nonterminals = [production.targets[0].id for production in productions]

        for production in productions:
            rule = Rule(production.targets[0].id, flatten(production.value, nonterminals))
            rules.add(rule)

        return Grammar(rules, productions[0].targets[0].id)

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
            print(production.number, repr(production))
        print("---")

    def productions_for_symbol(self, symbol):
        if symbol.key not in self._productions_for_symbol:
            self._productions_for_symbol[symbol.key] = OrderedSet([p for p in self.productions if p.left == symbol.key])
        return self._productions_for_symbol.get(symbol.key)

    def productions_with_symbol(self, symbol):
        if symbol.key not in self._productions_with_symbol:
            self._productions_with_symbol[symbol.key] = OrderedSet([p for p in self.productions if symbol.key in p.rightkeys])
        return self._productions_with_symbol.get(symbol.key)
