from state import State

class Item(object):
    def __init__(self, production, dot, grammar, collection, sgen, lookahead=None):
        self.production = production
        self.dot = dot
        self.grammar = grammar
        self.collection = collection
        self.sgen = sgen
        self.lookahead = lookahead or set()

        self.closured = False
        self.state = None

    def should_closure(self):
        return not self.closured  # TODO

    def closure(self):
        if not self.should_closure():
            return None
        if not self.state:
            self.state = State(
                [self], self.grammar, self.collection, self.sgen
            )
        return self.state
