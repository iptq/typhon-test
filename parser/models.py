from collections import OrderedDict
from copy import deepcopy

from parser.orderedset import OrderedSet, ItemSet, StateCollection
from parser.symbols import *
from parser.utils import color


class CanonicalCollection(object):
    def __init__(self, grammar):
        self.grammar = grammar
        self.intermediate_states = StateCollection()
        self.final_states = StateCollection()
        self.kernel_sets_transitions = dict()
        self.lr0sets = dict()
        self._states = None

        self.root_item = Item(self.grammar.augmented, 0, self.grammar, self, SetGenerator(
            grammar), OrderedSet([GEOF()]))
        self.root_item.closure().goto()

        self.remap()
        self.compress()

        # self.print()

    def remap(self):
        self._states = OrderedSet(
            list(self.intermediate_states) + list(self.final_states))
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
        except:
            pass

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


class Item(object):
    def __init__(self, production, dot, grammar, collection, set_generator, lookahead_set=None):
        self.production = production
        self.right = self.production.right
        self.dot = dot
        self.grammar = grammar
        self.collection = collection
        self.set_generator = set_generator
        self._lookahead_set = lookahead_set

        self.outer_state = None
        self.closured = False
        self.state = None

    def __repr__(self):
        items = []
        for item in self.production.right:
            items.append(repr(item))
        items.insert(self.dot, ".")
        return "Item({} -> {}) lookahead[{}]".format(
            self.production.left,
            " ".join(items),
            ",".join(['"{}"'.format(x.key) for x in self.lookahead_set]))

    @property
    def key(self):
        return "{}|{}|{}".format(
            self.production.number,
            self.dot,
            self.lookahead_set_key)

    @property
    def lr0_key(self):
        return "{}|{}".format(self.production.number, self.dot)

    @property
    def is_connected(self):
        return self.outer_state is not None

    @property
    def current_symbol(self):
        return self.right[self.dot]

    @property
    def is_epsilon(self):
        return self.current_symbol == GEPSILON()

    @property
    def is_shift(self):
        return not self.is_final and self.grammar.is_token(self.current_symbol)

    @property
    def is_reduce(self):
        return self.is_final and not self.production.augmented

    @property
    def is_final(self):
        return self.dot == len(self.right) or self.is_epsilon

    @property
    def goto(self):
        if not self.outer_state:
            self.state.goto()
        return self.outer_state

    def __hash__(self):
        return hash(self.key)

    def merge(self, other):
        self._lookahead_set = self.lookahead_set.union(other.lookahead_set)

    def calc_lookahead_set(self):
        previous = deepcopy(self._lookahead_set) or OrderedSet()
        lookahead_set = None
        follow = self.dot + 1
        rhs = self.production.right
        if follow < len(rhs):
            lookahead_part = rhs[follow:]
            lookahead_set = self.set_generator.first_of_rhs(lookahead_part)
        epsilon = False
        if lookahead_set:
            epsilon = GEPSILON() in lookahead_set
            if epsilon:
                lookahead_set.remove(GEPSILON())
        else:
            lookahead_set = OrderedSet()

        if not lookahead_set or epsilon:
            lookahead_set = previous
        return lookahead_set

    @property
    def lookahead_set(self):
        if not self._lookahead_set:
            self._lookahead_set = self.calc_lookahead_set()
        return self._lookahead_set

    @property
    def lookahead_set_key(self):
        keys = list(map(lambda v: v.key, self._lookahead_set))
        keys.sort()
        return ",".join(keys)

    def connect(self, state):
        self.outer_state = state

    def should_closure(self):
        return (not self.closured and
                not self.is_final and
                self.current_symbol.key in self.grammar.nonterminals)

    def closure(self):
        if not self.should_closure():
            return

        if not self.state:
            self.state = State(ItemSet([self]), self.grammar, self.collection)

        productions = self.grammar.productions_for_symbol(self.current_symbol)
        items = ItemSet([Item(production, 0, self.grammar, self.collection,
                              self.set_generator, self.calc_lookahead_set()) for production in productions])

        self.closured = True
        self.state.add(items)
        return self.state

    def advance(self):
        return Item(self.production, self.dot + 1, self.grammar, self.collection, self.set_generator, self.lookahead_set)


class ParseTable(object):
    def __init__(self, collection, grammar, verbose=False):
        global _verbose
        _verbose = verbose
        self.collection = collection
        self.grammar = grammar
        self.action = list(self.grammar.terminals) + [GEOF()]

        self.table = dict()
        self.state_conflict_data = dict()
        self.build()
        if verbose:
            self.print()

    def print(self):
        self.grammar.print()
        rows = [
            [""] + sorted([symbol.key for symbol in self.action]
                          ) + sorted(self.grammar.nonterminals)
        ]
        columns = [len(s) for s in rows[0]]
        for i in range(len(self.collection.states)):
            row = self.table[i]
            tablerow = [" {}".format(i)]
            # for symbol in self.action:
            #     entry = self.table[i].get(symbol.key, "")
            #     tablerow.append(entry)
            # for nonterminal in self.grammar.nonterminals:
            #     entry = self.table[i].get(nonterminal, "")
            #     tablerow.append(entry)
            for key in rows[0][1:]:
                tablerow.append(row.get(key, ""))

            assert len(columns) == len(tablerow)
            rows.append(tablerow)
            for j, col in enumerate(tablerow):
                if len(col) > columns[j]:
                    columns[j] = len(col)

        def get_row(row, first=False, nocolor=False):
            parts = []
            for i, col in enumerate(row):
                entry = col.rjust(columns[i], " ")
                if not nocolor and (i == 0 or first):
                    entry = color(entry, fg_blue=True, bold=True)
                if col == "acc":
                    entry = color(entry, fg_green=True)
                parts.append(entry)
            rowstr = " {} ".format(color("|", fg_dark_grey=True)).join(parts)
            border = color("|", fg_dark_grey=True)
            return "{}{} {}".format(border, rowstr, border)
        parts = []
        top = color(
            "+{}-+".format("-+-".join("-" * col for col in columns)), fg_dark_grey=True)
        sep = color(
            "+{}-+".format("-+-".join("-" * col for col in columns)), fg_dark_grey=True)
        bot = color(
            "+{}-+".format("-+-".join("-" * col for col in columns)), fg_dark_grey=True)
        for i, row in enumerate(rows):
            if i == 0:
                firstrow = get_row(row, first=True)
                parts.append(firstrow)
            else:
                parts.append(get_row(row))
        print(top)
        print("\n{}\n".format(sep).join(parts))
        print(bot)

    def should_reduce(self, item, terminal):
        return terminal in item.lookahead_set

    def build(self):
        def put_action_entry(row, column, entry):
            previous = row.get(column)
            if previous == entry:
                return
            if previous:
                parts = previous.split("/")
                if entry not in parts:
                    parts.append(entry)
                entry = "/".join(parts)
            row[column] = entry
        for state in self.collection.states:
            row = dict()
            conflicts = False
            for item in state.items:
                production = item.production
                if item.is_final:
                    if production.augmented:
                        row[GEOF().key] = "acc"
                    else:
                        for terminal in self.action:
                            # print(self.should_reduce(item, terminal), item, terminal)
                            if self.should_reduce(item, terminal):
                                put_action_entry(
                                    row, terminal.key, "r{}".format(production.number))
                else:
                    transition = item.current_symbol
                    next_state = item.goto

                    if self.grammar.is_token(transition):
                        put_action_entry(row, transition.key,
                                         "s{}".format(next_state.number))
                    else:
                        row[transition.key] = "{}".format(next_state.number)
            self.resolve_conflicts(state, row)
            self.table[state.number] = row

    def resolve_conflicts(self, state, row):
        for symbol, entry in row.items():
            choices = sorted(entry.split("/"))
            if len(choices) < 2:
                continue
            self.init_symbol_conflict_data(state, symbol, choices)
            if set(map(lambda f: f[0], choices)) == set(["r", "s"]):
                self.resolve_sr_conflict(state, row, symbol)
            elif set(map(lambda f: f[0], choices)) == set(["r"]):
                self.resolve_rr_conflict(state, row, symbol)

    def init_symbol_conflict_data(self, state, symbol, conflict):
        self.state_conflict_data[state, symbol] = conflict

    def resolve_sr_conflict(self, state, row, symbol):
        entry = row[symbol]
        # don't really have operator precedence impleneted yet so just shift LO
        row[symbol] = self.state_conflict_data[state, symbol][1]
        del self.state_conflict_data[state, symbol]

    def resolve_rr_conflict(self, state, row, symbol):
        entry = self.state_conflict_data[state, symbol]
        numbers = list(map(lambda f: int(f[1:]), entry))
        numbers.sort()
        # pick the smaller one LO
        row[symbol] = "r{}".format(numbers[0])
        del self.state_conflict_data[state, symbol]


class State(object):
    def __init__(self, kernel_items, grammar, collection):
        self.kernel_items = kernel_items
        self.grammar = grammar
        self.collection = collection

        self.lr0map = dict()
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
        tagstr = ", ".join(tags)
        items = []
        for item in self.items:
            res = " - {}".format(repr(item))
            tags = []
            if item in self.kernel_items:
                tags.append("kernel")
            if item.is_final:
                tags.append("final")
            if item.is_shift:
                tags.append("shift")
            if item.is_reduce:
                tags.append("reduce by production {}".format(
                    item.production.number))
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
        return self.kernel_items.key

    def get_transition_info(self, item):
        if item not in self.items:
            raise Exception("item not in state")
        if item.is_final:
            raise Exception("item is final")
        return self.transitions_for_symbol.get(item.current_symbol)

    def merge_two_items(self, first, second):
        transition = self.get_transition_info(
            first) if not first.is_final else None
        if transition:
            transition["items"].remove(first)
        self.items.remove(first)
        first.merge(second)
        self.items.remove(second)
        self.kernel_items.remove(second)
        if transition:
            transition["items"].remove(second)
        self.items.add(first)
        if transition:
            transition["items"].add(first)

    def merge_items(self):
        for key, items in self.lr0map.items():
            root_item = items[0]
            while len(items) > 1:
                self.merge_two_items(root_item, items.pop())

    def merge(self, other):
        if len(other.items) != len(self.items):
            raise Exception("states incompatible ({} vs {})".format(
                len(self.items), len(other.items)))
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
            self.transitions_for_symbol[symbol] = dict(
                items=ItemSet(), state=state)

        if item.key not in self.transitions_for_symbol[symbol]["items"]:
            self.transitions_for_symbol[symbol]["items"].add(item)
        if state:
            self.transitions_for_symbol[symbol]["state"] = state
            item.connect(state)

    def goto(self):
        if self.visited:
            return

        if not self.transitions_for_symbol:
            self.transitions_for_symbol = OrderedDict()
            for item in self.items:
                if item.is_final:
                    continue
                self.set_symbol_transition(item, None)

        for symbol in self.transitions_for_symbol:
            if self.transitions_for_symbol[symbol]["state"] is not None:
                continue
            items = self.transitions_for_symbol[symbol]["items"]
            outer_state = self.collection.get_transition_for_items(items)
            if not outer_state:
                outer_state = State(
                    ItemSet([item.advance() for item in items]), self.grammar, self.collection)
                self.collection.register_transition(items, outer_state)
            for item in items:
                self.set_symbol_transition(item, outer_state)

        self.visited = True
        for symbol in self.transitions_for_symbol:
            self.transitions_for_symbol[symbol]["state"].goto()


class SetGenerator(object):
    def __init__(self, grammar):
        self.grammar = grammar
        self.first_sets = dict()
        self.follow_sets = dict()

    def build_set(self, func):
        result = dict()
        for production in self.grammar.productions:
            app = func(GNT(production.left))
            result.update({production.left: app})
        return result

    def first_of(self, symbol):
        if symbol.key in self.first_sets:
            return self.first_sets[symbol.key]
        firstset = self.first_sets[symbol.key] = OrderedSet()
        if symbol.terminal or symbol.is_epsilon or isinstance(symbol, GEOF):
            firstset.add(symbol)
            return self.first_sets[symbol.key]
        else:
            productions = self.grammar.productions_for_symbol(symbol)
            for production in productions:
                first_of_rhs = self.first_of_rhs(production.right)
                firstset.merge(first_of_rhs)
        return firstset

    def first_of_rhs(self, rhs):
        firstset = OrderedSet()
        EPSILON = GEPSILON()
        for i, symbol in enumerate(rhs):
            if symbol.is_epsilon:
                firstset.add(EPSILON)
                break
            first_of_current = self.first_of(symbol)
            firstset.merge(first_of_current, exclude=[EPSILON])
            if EPSILON not in first_of_current:
                break
            elif i == len(rhs) - 1:
                firstset.add(EPSILON)
        return firstset

    def get_first_sets(self):
        return self.build_set(self.first_of)

    def follow_of(self, symbol):
        if symbol.key in self.follow_sets:
            return self.follow_sets[symbol.key]
        followset = self.follow_sets[symbol.key] = OrderedSet()
        if symbol == self.grammar.start:
            followset.add(GEOF())
        for production in self.grammar.productions_with_symbol(symbol):
            print("searching", production)
            rhs = deepcopy(production.right)
            symbols = OrderedSet(production.right)
            ind = rhs.index(symbol)
            while True:
                followpart = rhs[ind + 1:]
                if len(followpart) > 0:
                    while len(followpart) > 0:
                        sym = followpart[0]
                        first_of_follow = self.first_of(sym)
                        followset.merge(first_of_follow, exclude=[GEPSILON()])
                        if GEPSILON() not in first_of_follow:
                            break
                        followpart = followpart[1:]
                if len(followpart) == 0:
                    lhs = GNT(production.left)
                    if lhs != symbol:
                        followset.merge(self.follow_of(lhs))
                rhs = followpart
                try:
                    ind = rhs.index(symbol)
                except:
                    break
        return followset

    def get_follow_sets(self):
        return self.build_set(self.follow_of)
