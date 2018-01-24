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
        self.lr0sets = dict()
        self._states = None

        self.root_item = Item(self.grammar.augmented, 0, self.grammar, self, SetGenerator(grammar), OrderedSet([GEOF()]))
        self.root_item.closure().goto()

        self.remap()
        self.compress()
        self.print()

    def remap(self):
        self._states = OrderedSet(list(self.intermediate_states) + list(self.final_states))
        for i, state in enumerate(self.states):
            state.number = i
        return self._states

    def print(self):
        for state in self.states:
            print(state)

    @property
    def states(self):
        if not self._states:
            self.remap()
        return self._states

    def get_transition_for_items(self, items):
        return self.kernel_sets_transitions.get(items.key)

    def register_transition(self, items, state):
        self.kernel_sets_transitions[items.key] = state

    def register(self, state):
        (self.final_states if state.is_final else self.intermediate_states).add(state)
        key = state.kernel_items.lr0_key
        if key not in self.lr0sets:
            self.lr0sets[key] = OrderedSet()
        self.lr0sets[key].add(state)

    def unregister(self, state):
        (self.final_states if state.is_final else self.intermediate_states).remove(state)
        try:
            del self.kernel_sets_transitions[state.kernel_items.key]
            self.lr0sets[state.kernel_items.lr0_key].remove(state)
        except: pass

    def compress(self):
        for key, states in self.lr0sets.items():
            root_state = states[0]
            root_state.merge_items()
            while len(states) > 1:
                state = states.pop()
                state.merge_items()
                root_state.merge(state)
            for item in root_state.items:
                if item.is_connected:
                    outer_states = self.lr0sets[item.goto.kernel_items.lr0_key]
                    outer_state = outer_states[0]
                    item.connect(outer_state)
        self.remap()