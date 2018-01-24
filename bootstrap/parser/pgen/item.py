from grammar.symbols import *
from orderedset import OrderedSet

class ItemSet(OrderedSet):
    @property
    def key(self):
        if not self._key:
            self._key = "|".join(item.key for item in self.elements)
        return self._key

    @property
    def lr0_key(self):
        if not self._lr0_key:
            keys = OrderedSet(item.lr0_key for item in self.elements)
            self._lr0_key = "|".join(keys)
        return self._lr0_key

import state

class Item(object):
    def __init__(self, production, dot, grammar, collection, set_generator, lookahead_set=None):
        self.production = production
        self.right = self.production.right
        self.dot = dot
        self.grammar = grammar
        self.collection = collection
        self.set_generator = set_generator
        self._lookahead_set = lookahead_set

        self.outer_state = None
        self.closured = False
        self.state = None

    def __repr__(self):
        items = []
        for item in self.production.right:
            items.append(repr(item))
        items.insert(self.dot, ".")
        return "Item({} -> {}) lookahead[{}]".format(
            self.production.left,
            " ".join(items),
            ",".join(['"{}"'.format(x.key) for x in self.lookahead_set]))

    @property
    def key(self):
        return "{}|{}|{}".format(
            self.production.number,
            self.dot,
            self.lookahead_set_key)

    @property
    def lr0_key(self):
        return "{}|{}".format(self.production.number, self.dot)
    
    @property
    def is_connected(self):
        return self.outer_state is not None
    
    @property
    def current_symbol(self):
        return self.right[self.dot]

    @property
    def is_epsilon(self):
        return self.current_symbol == GEPSILON()

    @property
    def is_shift(self):
        return not self.is_final and self.grammar.is_token(self.current_symbol)

    @property
    def is_reduce(self):
        return self.is_final and not self.production.augmented
    
    @property
    def is_final(self):
        return self.dot == len(self.right) or self.is_epsilon

    @property
    def goto(self):
        if not self.outer_state:
            self.state.goto()
        return self.outer_state

    def __hash__(self):
        return hash(self.key)

    def merge(self, other):
        self._lookahead_set = self.lookahead_set.union(other.lookahead_set)

    def calc_lookahead_set(self):
        previous = self._lookahead_set or OrderedSet()
        lookahead_set = None
        follow = self.dot + 1
        rhs = self.production.right
        if follow < len(rhs):
            lookahead_part = rhs[follow:]
            lookahead_set = self.set_generator.first_of_rhs(lookahead_part)
        epsilon = False
        EPSILON = GEPSILON()
        if lookahead_set:
            epsilon = EPSILON in lookahead_set
            if epsilon: del lookahead_set[EPSILON]
        else:
            lookahead_set = OrderedSet()

        if not lookahead_set or epsilon:
            lookahead_set = previous
        return lookahead_set

    @property
    def lookahead_set(self):
        if not self._lookahead_set:
            self._lookahead_set = self.calc_lookahead_set()
        return self._lookahead_set

    @property
    def lookahead_set_key(self):
        keys = list(map(lambda v: v.key, self._lookahead_set))
        keys.sort()
        return ",".join(keys)
    

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
            self.state = state.State(ItemSet([self]), self.grammar, self.collection)

        productions = self.grammar.productions_for_symbol(self.current_symbol)
        items = [Item(production, 0, self.grammar, self.collection, self.set_generator, self.calc_lookahead_set()) for production in productions]

        self.closured = True
        self.state.add(items)
        return self.state

    def advance(self):
        return Item(self.production, self.dot + 1, self.grammar, self.collection, self.set_generator, self.lookahead_set)
