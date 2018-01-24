from copy import deepcopy
from grammar.symbols import *

class SetGenerator(object):
    def __init__(self, grammar):
        self.grammar = grammar
        self.first_sets = dict()
        self.follow_sets = dict()

    def build_set(self, func):
        return dict([(production.left, func(GNT(production.left))) for production in self.grammar.productions])

    def first_of(self, symbol):
        if symbol.key in self.first_sets:
            return self.first_sets[symbol.key]
        firstset = self.first_sets[symbol.key] = set()
        if symbol.terminal:
            firstset.add(symbol)
        else:
            productions = self.grammar.productions_for_symbol(symbol)
            for production in productions:
                firstset = firstset.union(self.first_of_rhs(production.right))
        self.first_sets[symbol.key] = firstset
        return firstset

    def first_of_rhs(self, rhs):
        firstset = set()
        EPSILON = GEPSILON()
        for i, symbol in enumerate(rhs):
            if isinstance(symbol, GEPSILON):
                firstset.add(EPSILON)
                break
            firstcurrent = self.first_of(symbol)
            firstset = firstset.union(firstcurrent)
            if EPSILON not in firstcurrent:
                break
            elif i == len(rhs) - 1:
                firstset.add(EPSILON)
        return firstset

    def follow_of(self, symbol):
        if symbol.key in self.follow_sets:
            return self.follow_sets[symbol.key]
        followset = self.follow_sets[symbol.key] = set()
        if symbol == self.grammar.start:
            followset.add(GEOF())
        for production in self.grammar.productions_with_symbol(symbol):
            rhs = deepcopy(production.right)
            symbols = set(production.right)
            ind = rhs.index(symbol)
            while True:
                followpart = rhs[ind + 1:]
                if len(followpart) > 0:
                    while len(followpart) > 0:
                        sym = followpart[0]
                        first_of_follow = self.first_of(sym)
                        followset = followset.union(filter(lambda s: s != GEPSILON(), first_of_follow))
                        if GEPSILON() not in first_of_follow:
                            break
                        followpart = followpart[1:]
                if len(followpart) == 0:
                    lhs = GNT(production.left)
                    if lhs != symbol:
                        followset = followset.union(self.follow_of(lhs))
                rhs = followpart
                try:
                    ind = rhs.index(symbol)
                except:
                    break
        self.follow_sets[symbol.key] = followset
        return followset
