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
        for i, item in enumerate(self.production.right):
            if i == self.dot:
                items.append(".")
            items.append(repr(item))
        return "{} -> {}".format(self.production.left, " ".join(items))

    @property
    def key(self):
        return "{}|{}".format(self.production.number, self.dot)
    
    @property
    def current_symbol(self):
        return self.right[self.dot]
    
    @property
    def is_final(self):
        return self.dot == len(self.right)

    def should_closure(self):
        return (not self.closured and
            not self.is_final and
            self.current_symbol in self.grammar.nonterminals)

    def closure(self):
        if not self.should_closure():
            return

        if not self.state:
            self.state = State(self.grammar, self.collection)

        productions = self.grammar.get_productions_for_symbol(self.current_symbol)
        items = [Item(production, 0, self.grammar, self.collection) for production in productions]

        self.closured = True
        self.state.add(items)
        return self.state
