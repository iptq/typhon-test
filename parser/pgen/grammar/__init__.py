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
        self.nonterminals = productions.keys()
        self.augmented = Production(0, "$accept", [start], 0, self)
        self.augmented.augmented = True
        self.productions = [self.augmented]
        for nonterminal, rules in productions.items():
            for i, production in enumerate(rules):
                self.productions.append(Production(i, nonterminal, production, len(self.productions), self))

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

    def get_productions_for_symbol(self, symbol):
        if symbol not in self.productions_for_symbol:
            self.productions_for_symbol[symbol] = [p for p in self.productions if p.left == symbol]
        return self.productions_for_symbol[symbol]