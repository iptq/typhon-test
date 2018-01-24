from grammar.symbols import *
import colors

class ParseTable(object):
    def __init__(self, collection, grammar):
        self.collection = collection
        self.grammar = grammar
        self.action = list(self.grammar.terminals) + [GEOF()]

        self.table = dict()
        self.build()
        self.print()

    def print(self):
        rows = [
            [""] + sorted([symbol.key for symbol in self.action]) + sorted(self.grammar.nonterminals)
        ]
        columns = [len(s) for s in rows[0]]
        for i, row in self.table.items():
            tablerow = [" {}".format(i)]
            for symbol in self.action:
                entry = self.table[i].get(symbol.key, "")
                tablerow.append(entry)
            for nonterminal in self.grammar.nonterminals:
                entry = self.table[i].get(nonterminal, "")
                tablerow.append(entry)
            assert len(columns) == len(tablerow)
            rows.append(tablerow)
            for i, col in enumerate(tablerow):
                if len(col) > columns[i]:
                    columns[i] = len(col)
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

    def build(self):
        for state in self.collection.states:
            row = dict()
            conflicts = False
            for item in state.items:
                if item.is_final:
                    if item.production.augmented:
                        row["EOF"] = "acc"
            self.table[state.number] = row