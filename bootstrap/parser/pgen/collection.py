from item import Item

class CanonicalCollection(object):
    def __init__(self, grammar):
        self.grammar = grammar
        self.intermediate_states = dict()
        self.final_states = dict()

        self.root_item = Item(self.grammar.augmented, 0, self.grammar, self)
        self.root_item.closure().goto()

        print("States:")
        for state in self.states:
            print(repr(state))

    @property
    def states(self):
        states = list(self.intermediate_states.values()) + list(self.final_states.values())
        for i, state in enumerate(states):
            state.number = i
        return states

    def register(self, state):
        (self.final_states if state.is_final else self.intermediate_states)[state.key] = state
