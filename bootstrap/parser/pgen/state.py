from item import ItemSet

class State(object):
    def __init__(self, kernel_items, grammar, collection):
        self.kernel_items = kernel_items
        self.grammar = grammar
        self.collection = collection

        self.items = ItemSet()
        self.visited = False
        self.number = None
        self.add(self.kernel_items)

        self.transitions_for_symbol = None
        self.collection.register(self)

    def __repr__(self):
        tags = []
        if self.is_final:
            tags.append("final")
        items = "\n".join([" - {}".format(repr(item)) for item in self.items])
        return "State {}: {}\n{}".format(self.number, ", ".join(tags), items)

    @property
    def is_final(self):
        return len(self.items) == 1 and self.items[0].is_final

    @property
    def is_accept(self):
        return self.is_final and self.items[0].production.augmented
    
    @property
    def key(self):
        #hack?
        return id(self)    

    def add(self, obj):
        if type(obj) is list:
            for item in obj:
                self.add(item)
            return
        if obj in self.items:
            return
        self.items.add(obj) 
        obj.state = self
        obj.closure()

    def set_symbol_transition(self, item, state):
        symbol = item.current_symbol
        if symbol not in self.transitions_for_symbol:
            self.transitions_for_symbol[symbol] = dict(items=dict(), state=state)
        if item.key not in self.transitions_for_symbol[symbol]:
            self.transitions_for_symbol[symbol]["items"][item.key] = item
        if state:
            self.transitions_for_symbol[symbol]["state"] = state
            item.connect(state)

    def goto(self):
        if self.visited:
            return

        if not self.transitions_for_symbol:
            self.transitions_for_symbol = dict()
            for item in self.items:
                if item.is_final: continue
                self.set_symbol_transition(item, None)

        for symbol in self.transitions_for_symbol:
            if self.transitions_for_symbol[symbol]["state"] is not None:
                continue
            items = list(self.transitions_for_symbol[symbol]["items"].values())
            outer_state = self.collection.get_transition_for_items(set(items))
            if not outer_state:
                outer_state = State([item.advance() for item in items], self.grammar, self.collection)
                self.collection.register_transition(items, outer_state)
            for item in items:
                self.set_symbol_transition(item, outer_state)

        self.visited = True
        for symbol in self.transitions_for_symbol:
            self.transitions_for_symbol[symbol]["state"].goto()
