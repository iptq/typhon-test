from grammar.symbols import *
import colors
from set_generator import SetGenerator

class ParseTable(object):
    def __init__(self, collection, grammar):
        self.collection = collection
        self.grammar = grammar
        self.action = list(self.grammar.terminals) + [GEOF()]

        self.table = dict()
        self.build()
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
        print(rows)
        def get_row(row, first=False, nocolor=False):
            parts = []
            for i, col in enumerate(row):
                entry = col.ljust(columns[i], " ")
                if not nocolor and (i == 0 or first):
                    entry = colors.color(entry, fg_blue=True, bold=True)
                if col == "acc":
                    entry = colors.color(entry, fg_green=True)
                parts.append(entry)
            rowstr = " {} ".format(colors.color("│", fg_dark_grey=True)).join(parts)
            border = colors.color("│", fg_dark_grey=True)
            return "{}{} {}".format(border, rowstr, border)
        parts = []
        top = colors.color("┌{}─┐".format("─┬─".join(["─" * col for col in columns])), fg_dark_grey=True)
        sep = colors.color("├{}─┤".format("─┼─".join(["─" * col for col in columns])), fg_dark_grey=True)
        bot = colors.color("└{}─┘".format("─┴─".join(["─" * col for col in columns])), fg_dark_grey=True)
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
                    parts.push(entry)
                entry = "/".join(parts)
            row[column] = entry
        for state in self.collection.states:
            row = dict()
            conflicts = False
            for item in state.items:
                production = item.production
                if item.is_final:
                    if production.augmented:
                        row["EOF"] = "acc"
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
            self.table[state.number] = row