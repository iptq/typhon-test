import ast
from copy import deepcopy
from functools import reduce
from operator import xor

from parser.orderedset import OrderedSet, ItemSet
from parser.symbols import *

# generate grammar parser
try:
    import generated_ebnf_parser
except Exception:
    """
    with open(os.path.join(os.path.dirname(__file__), "EBNF.g"), "r") as f:
        ebnf_grammar = f.read()
    sys.path.append(os.path.realpath(os.path.dirname(os.path.dirname(__file__))))
    from parser.pgen.generator import ParserGenerator
    print("GRAMMAR:", ebnf_grammar)
    """


class Production(object):
    def __init__(self, ind, left, right, number, grammar):
        self.ind = ind
        self.left = GNT(left)
        self.right = right
        self.number = number
        self.grammar = grammar
        self.augmented = False

        self.right_set = ItemSet(self.right)
        self._semantic_action = None

    def __hash__(self):
        return reduce(xor, map(hash, [self.left, *self.right, id(self.grammar)]))

    def __repr__(self):
        left = repr(self.left)
        right = " + ".join([repr(sym) for sym in self.right])
        if self.ind == 0:
            return "{} -> {}".format(left, right)
        else:
            pad = " " * (len(left) + len("->"))
            return "{}| {}".format(pad, right)


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
                obj = Production(i, nonterminal, production,
                                 len(self.productions), self)
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
            rule = Rule(production.targets[0].id, flatten(
                production.value, nonterminals))
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
            self._productions_for_symbol[symbol.key] = OrderedSet(
                [p for p in self.productions if p.left == symbol.key])
        return self._productions_for_symbol.get(symbol.key)

    def productions_with_symbol(self, symbol):
        if symbol.key not in self._productions_with_symbol:
            self._productions_with_symbol[symbol.key] = OrderedSet(
                [p for p in self.productions if symbol in p.right_set])
        return self._productions_with_symbol.get(symbol.key)


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
            elif isinstance(node, ast.Set):
                current.append(None)
            elif isinstance(node, ast.List):
                # syntactic sugar for EMPTY, {b}
                flat = flatten(
                    ast.Tuple([ast.Name("EMPTY", node.ctx), ast.Set(node.elts)], node.ctx), front)
                current.append(flat)
            elif isinstance(node, ast.Name):
                if node.id == "IDENT":
                    obj = GIdent()
                elif node.id == "NUMBER":
                    obj = GNum()
                elif node.id == "STRING":
                    obj = GStr()
                elif node.id == "EMPTY":
                    obj = GEPSILON()
                elif node.id == "EOF":
                    obj = GEOF()
                elif node.id == "NEWLINE":
                    obj = GNEWLINE()
                elif node.id == "INDENT":
                    obj = GINDENT()
                elif node.id == "DEDENT":
                    obj = GDEDENT()
                elif node.id in nonterminals:
                    obj = GNT(node.id)
                else:
                    raise NotImplementedError(
                        "{} not implemented".format(node.id))
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


def repeat():
    return
