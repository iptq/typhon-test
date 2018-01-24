class ItemSet(object):
    def __init__(self):
        self.elements = []
        self.map = dict()

    def add(self, item):
        if item.key in self.map:
            return
        self.map[item.key] = len(self.elements)
        self.elements.append(item)

    def __contains__(self, item):
        return item.key in self.map

    def __len__(self):
        return len(self.elements)

    def __getitem__(self, key):
        if type(key) is int:
            return self.elements[key]
        elif type(key) is str:
            return self.elements[self.map[key]]

    def __iter__(self):
        for item in self.elements:
            yield item

    def __repr__(self):
        return "[{}]".format(", ".join([repr(item) for item in self.elements]))

from state import State

class Item(object):
    def __init__(self, production, dot, grammar, collection):
        self.production = production
        self.right = self.production.right
        self.dot = dot
        self.grammar = grammar
        self.collection = collection

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

        productions = self.grammar.get_productions_for_symbol(self.current_symbol)
        items = [Item(production, 0, self.grammar, self.collection) for production in productions]

        self.closured = True
        self.state.add(items)
        return self.state

    def advance(self):
        return Item(self.production, self.dot + 1, self.grammar, self.collection)
