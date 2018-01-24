from collections import OrderedDict
from orderedset import OrderedSet
import item as ItemModule

class State(object):
    def __init__(self, kernel_items, grammar, collection):
        self.kernel_items = kernel_items
        self.grammar = grammar
        self.collection = collection

        self.lr0map = dict()
        self.items = ItemModule.ItemSet()
        self.visited = False
        self.number = None
        self.add(self.kernel_items)

        self.transitions_for_symbol = None
        self.collection.register(self)

    def __repr__(self):
        tags = []
        if self.is_final:
            tags.append("final")
        tagstr = ", ".join(tags)
        items = []
        for item in self.items:
            res = " - {}".format(repr(item))
            tags = []
            if item in self.kernel_items:
                tags.append("kernel")
            if item.is_shift:
                tags.append("shift")
            if item.is_reduce:
                tags.append("reduce by production {}".format(item.production.number))
            if item.is_final and not item.is_reduce:
                tags.append("accept")
            if item.goto:
                tags.append("goes to state {}".format(item.goto.number))
            if tags:
                res += " ({})".format(", ".join(tags))
            items.append(res)
        itemstr = "\n".join(items)
        return "State {}: {}\n{}".format(self.number, tagstr, itemstr)

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

    def get_transition_info(self, item):
        if item not in self.items:
            raise Exception("item not in state")
        if item.is_final:
            raise Exception("item is final")
        return self.transitions_for_symbol.get(item.current_symbol)

    def merge_two_items(self, first, second):
        transition = self.get_transition_info(first) if not first.is_final else None
        if transition:
            del transition["items"][first.key]
        self.items.remove(first)
        first.merge(second)
        self.items.remove(second)
        self.kernel_items.remove(second)
        if transition:
            del transition["items"][second.key]
        self.items.add(first)
        if transition:
            transition["items"][first.key] = first

    def merge_items(self):
        for key, items in self.lr0map.items():
            root_item = items[0]
            while len(items) > 1:
                self.merge_two_items(root_item, items.pop())

    def merge(self, other):
        if len(other.items) != len(self.items):
            raise Exception("states incompatible ({} vs {})".format(len(self.items), len(other.items)))
        if self.kernel_items.key != other.kernel_items.key:
            for a, b in zip(self.items, other.items):
                a.merge(b)
        self.collection.unregister(other)

    def add(self, obj):
        if type(obj) is list or isinstance(obj, OrderedSet):
            for item in obj:
                self.add(item)
            return
        if obj in self.items:
            return
        if self.items.add(obj):
            if obj.lr0_key not in self.lr0map:
                self.lr0map[obj.lr0_key] = OrderedSet()
            self.lr0map[obj.lr0_key].add(obj)
            obj.state = self
            obj.closure()

    def set_symbol_transition(self, item, state):
        symbol = item.current_symbol
        if symbol not in self.transitions_for_symbol:
            self.transitions_for_symbol[symbol] = dict(items=OrderedDict(), state=state)
        if item.key not in self.transitions_for_symbol[symbol]:
            self.transitions_for_symbol[symbol]["items"][item.key] = item
        if state:
            self.transitions_for_symbol[symbol]["state"] = state
            item.connect(state)

    def goto(self):
        if self.visited:
            return

        if not self.transitions_for_symbol:
            self.transitions_for_symbol = OrderedDict()
            for item in self.items:
                if item.is_final: continue
                self.set_symbol_transition(item, None)

        for symbol in self.transitions_for_symbol:
            if self.transitions_for_symbol[symbol]["state"] is not None:
                continue
            items = ItemModule.ItemSet(self.transitions_for_symbol[symbol]["items"].values())
            outer_state = self.collection.get_transition_for_items(ItemModule.ItemSet(items))
            if not outer_state:
                outer_state = State(ItemModule.ItemSet([item.advance() for item in items]), self.grammar, self.collection)
                self.collection.register_transition(items, outer_state)
            for item in items:
                self.set_symbol_transition(item, outer_state)

        self.visited = True
        for symbol in self.transitions_for_symbol:
            self.transitions_for_symbol[symbol]["state"].goto()
