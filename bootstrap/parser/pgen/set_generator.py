from copy import deepcopy
from orderedset import OrderedSet
from grammar.symbols import *

EPSILON = GEPSILON()

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
        firstset = self.first_sets[symbol.key] = OrderedSet()
        if self.grammar.is_token(symbol) or isinstance(symbol, GEPSILON) or isinstance(symbol, GEOF):
            firstset.add(symbol)
            return firstset
        productions = self.grammar.productions_for_symbol(symbol)
        for production in productions:
            firstset = firstset.union(self.first_of_rhs(production.right))
            print(production, "###", firstset)
        return firstset

    def first_of_rhs(self, rhs):
        firstset = OrderedSet()
        for i, symbol in enumerate(rhs):
            if isinstance(symbol, GEPSILON):
                firstset.add(EPSILON)
                break
            firstcurrent = self.first_of(symbol)
            firstset = firstset.union(firstcurrent, exclude=[EPSILON])
            if EPSILON not in firstcurrent:
                break
            elif i == len(rhs) - 1:
                firstset.add(EPSILON)
        return firstset

    def follow_of(self, symbol):
        if symbol.key in self.follow_sets:
            return self.follow_sets[symbol.key]
        followset = self.follow_sets[symbol.key] = OrderedSet()
        if symbol == self.grammar.start:
            followset.add(GEOF())
        for production in self.grammar.productions_with_symbol(symbol):
            print("searching", production)
            rhs = deepcopy(production.right)
            symbols = OrderedSet(production.right)
            ind = rhs.index(symbol)
            while True:
                followpart = rhs[ind + 1:]
                if len(followpart) > 0:
                    while len(followpart) > 0:
                        sym = followpart[0]
                        first_of_follow = self.first_of(sym)
                        followset = followset.union(first_of_follow, exclude=EPSILON)
                        if not any(isinstance(x, GEPSILON) for x in first_of_follow):
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
        return followset
