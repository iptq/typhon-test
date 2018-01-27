from functools import reduce
from operator import xor
from orderedset import OrderedSet
import symbols
import item

class Production(object):
    def __init__(self, ind, left, right, number, grammar):
        self.ind = ind
        self.left = symbols.GNT(left)
        self.right = right
        self.number = number
        self.grammar = grammar
        self.augmented = False

        self.right_set = item.ItemSet(self.right)
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

