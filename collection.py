from item import Item
from sgen import SetsGenerator
from oset import OrderedSet

class CanonicalCollection(object):
    def __init__(self, grammar):
        self.grammar = grammar
        self._states = []
        self.intermediate_states = OrderedSet()
        self.final_states = OrderedSet()

        self.root_item = Item(
            grammar.augmented,
            0, self.grammar, self,
            SetsGenerator(self.grammar), set("$")
        )

        # ok build it
        self.root_item.closure().goto()

    @property
    def states(self):
        if not self._states:
            self.remap()
        return self._states

    def print(self):
        for state in self.states:
            state.print()

    def remap(self):
        self._states = OrderedSet(list(self.intermediate_states) + list(self.final_states))
        for i, state in enumerate(self._states):
            state.number = i
