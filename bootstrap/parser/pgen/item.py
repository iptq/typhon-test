from grammar.symbols import *
from orderedset import OrderedSet

class ItemSet(OrderedSet):
    pass

from state import State

class Item(object):
    def __init__(self, production, dot, grammar, collection, set_generator, lookahead_set=None):
        self.production = production
        self.right = self.production.right
        self.dot = dot
        self.grammar = grammar
        self.collection = collection
        self.set_generator = set_generator
        self._lookahead_set = lookahead_set

        self.closured = False
        self.state = None

    def __repr__(self):
        items = []
        for item in self.production.right:
            items.append(repr(item))
        items.insert(self.dot, ".")
        return "{} -> {}".format(self.production.left, " ".join(items))

    @staticmethod
    def set_key(items):
        return "|".join(item.key for item in set(items))

    @property
    def key(self):
        return "{}|{}".format(self.production.number, self.dot)
    
    @property
    def current_symbol(self):
        return self.right[self.dot]
    
    @property
    def is_final(self):
        return self.dot == len(self.right)

    @property
    def goto(self):
        if not self.outer_state:
            self.state.goto()
        return self.outer_state

    def lookahead_set(self, recalc=False):
        if recalc or not self._lookahead_set:
            previous = self._lookahead_set or set()
            follow = self.dot + 1
            rhs = self.production.right
            if follow < len(rhs):
                lookahead_part = rhs[follow:]
                self._lookahead_set = self.set_generator.first_of_rhs(rhs)
            epsilon = False
            EPSILON = GEPSILON()
            if self._lookahead_set:
                epsilon = EPSILON in self._lookahead_set
                if epsilon: del self._lookahead_set[EPSILON]
            else:
                self._lookahead_set = set()

            if not self._lookahead_set or epsilon:
                self._lookahead_set = previous
        return self._lookahead_set

    def connect(self, state):
        self.outer_state = state

    def should_closure(self):
        return (not self.closured and
            not self.is_final and
            self.current_symbol.key in self.grammar.nonterminals)

    def closure(self):
        if not self.should_closure():
            return

        if not self.state:
            self.state = State([self], self.grammar, self.collection)

        productions = self.grammar.productions_for_symbol(self.current_symbol)
        items = [Item(production, 0, self.grammar, self.collection, self.set_generator, self.lookahead_set(recalc=True)) for production in productions]

        self.closured = True
        self.state.add(items)
        return self.state

    def advance(self):
        return Item(self.production, self.dot + 1, self.grammar, self.collection, self.set_generator, self.lookahead_set())
