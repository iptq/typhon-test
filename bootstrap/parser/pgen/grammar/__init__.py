import ast
from copy import deepcopy

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

class Grammar(object):
    def __init__(self, productions, start):
        assert len(productions.get(start)) == 1
        
        self._terminals = None
        self._tokens = None

        self.nonterminals = list(productions.keys())

        self.augmented = Production(0, "$accept", [GNT(start)], 0, self)
        self.augmented.augmented = True
        self.productions = [self.augmented]
        for nonterminal, rules in productions.items():
            for i, production in enumerate(rules):
                self.productions.append(Production(i, nonterminal, production, len(self.productions), self))

        # print("Grammar Productions:")
        # for production in self.productions:
        #     print(repr(production))
        # print("---")
        self.productions_for_symbol = dict()

    @staticmethod
    def from_file(grammar_file):
        with open(grammar_file, "r") as f:
            data = f.read()

        rules = dict()
        productions = ast.parse(data).body
        nonterminals = [production.targets[0].id for production in productions]

        for production in productions:
            rules.update({ production.targets[0].id: flatten(production.value, nonterminals) })

        return Grammar(rules, productions[0].targets[0].id)

    @property
    def terminals(self):
        if not self._terminals:
            self._terminals = set()
            for production in self.productions:
                for symbol in production.right:
                    assert isinstance(symbol, GrammarSymbol)
                    if symbol.terminal:
                        self._terminals.add(symbol)
        return self._terminals

    @property
    def tokens(self):
        if not self._tokens:
            self._tokens = set()
            for production in self.productions:
                for symbol in production.right:
                    assert isinstance(symbol, GrammarSymbol)
                    if not symbol.terminal and symbol.key not in self.nonterminals:
                        self._tokens.add(symbol)
        return self._tokens
        

    def get_productions_for_symbol(self, symbol):
        if symbol.key not in self.productions_for_symbol:
            self.productions_for_symbol[symbol.key] = set([p for p in self.productions if p.left == symbol.key])
        return self.productions_for_symbol.get(symbol.key)