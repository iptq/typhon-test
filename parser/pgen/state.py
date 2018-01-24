class State(object):
    def __init__(self, grammar, collection):
        self.items = dict()
        self.visited = False
        self.grammar = grammar
        self.collection = collection
        self.number = None

        self.collection.register(self)

    def __repr__(self):
        tags = []
        if self.is_final:
            tags.append("final")
        items = "\n".join([" - {}".format(repr(item)) for item in self.items.values()])
        return "State {}: {}\n{}".format(self.number, ", ".join(tags), items)

    @property
    def is_final(self):
        return len(self.items.keys()) == 1 and list(self.items.values())[0].is_final

    @property
    def is_accept(self):
        return self.is_final and list(self.items.values())[0].production.augmented
    
    @property
    def key(self):
        #hack?
        return id(self)    

    def add(self, obj):
        if type(obj) is list:
            for item in obj:
                self.add(item)
                item.closure()
            return
        if obj.key in self.items:
            return
        self.items[obj.key] = obj
        obj.state = self

    def goto(self):
        if self.visited:
            return
        self.visited = True