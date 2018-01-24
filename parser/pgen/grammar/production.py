class Production(object):
    def __init__(self, ind, left, right, number, grammar):
        self.ind = ind
        self.left = left
        self.right = right
        self.number = number
        self.grammar = grammar
        self.augmented = False

    def __repr__(self):
        left = self.left
        right = " + ".join([repr(sym) for sym in self.right])
        if self.ind == 0:
            return "{} -> {}".format(left, right)
        else:
            pad = " " * (len(left) + len("->"))
            return "{}| {}".format(pad, right)
