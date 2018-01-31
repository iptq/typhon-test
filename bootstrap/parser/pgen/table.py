import os
import sys
sys.path.insert(0, os.path.realpath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

from grammar.symbols import *
from set_generator import SetGenerator

_verbose = False
colors = None
def color(*args, **kwargs):
    global colors
    if not _verbose: return
    if colors is None:
        import colors
    return colors.color(*args, **kwargs)

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
            [""] + sorted([symbol.key for symbol in self.action]) + sorted(self.grammar.nonterminals)
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
        top = color("+{}-+".format("-+-".join("-" * col for col in columns)), fg_dark_grey=True)
        sep = color("+{}-+".format("-+-".join("-" * col for col in columns)), fg_dark_grey=True)
        bot = color("+{}-+".format("-+-".join("-" * col for col in columns)), fg_dark_grey=True)
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
            if previous == entry: return
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
                                put_action_entry(row, terminal.key, "r{}".format(production.number))
                else:
                    transition = item.current_symbol
                    next_state = item.goto

                    if self.grammar.is_token(transition):
                        put_action_entry(row, transition.key, "s{}".format(next_state.number))
                    else:
                        row[transition.key] = "{}".format(next_state.number)
            self.resolve_conflicts(state, row)
            self.table[state.number] = row

    def resolve_conflicts(self, state, row):
        for symbol, entry in row.items():
            choices = sorted(entry.split("/"))
            if len(choices) < 2: continue
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
