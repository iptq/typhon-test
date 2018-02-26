class State(object):
    def __init__(self, kernel, grammar, collection, sgen):
        self.kernel = kernel
        self.grammar = grammar
        self.collection = collection
        self.sgen = sgen

        self.items = []
        self.number = None
        self.visited = False

    def goto(self):
        if self.visited:
            return
