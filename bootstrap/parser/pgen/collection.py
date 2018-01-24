from item import Item
from set_generator import SetGenerator
from orderedset import OrderedSet
from grammar.symbols import *

class StateCollection(OrderedSet): pass

class CanonicalCollection(object):
    def __init__(self, grammar):
        self.grammar = grammar
        self.intermediate_states = StateCollection()
        self.final_states = StateCollection()
        self.kernel_sets_transitions = dict()

        self.root_item = Item(self.grammar.augmented, 0, self.grammar, self, SetGenerator(grammar), set([GEOF()]))
        self.root_item.closure().goto()

    def remap(self):
        states = list(self.intermediate_states) + list(self.final_states)
        for i, state in enumerate(states):
            state.number = i
        return states

    @property
    def states(self):
        return self.remap()

    def get_transition_for_items(self, items):
        return self.kernel_sets_transitions.get(Item.set_key(items))

    def register_transition(self, items, state):
        self.kernel_sets_transitions[Item.set_key(items)] = state

    def register(self, state):
        (self.final_states if state.is_final else self.intermediate_states).add(state)
        self.remap()
