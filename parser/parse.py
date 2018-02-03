# pretty much direct port of https://github.com/DmitrySoshnikov/syntax

import os
from copy import deepcopy
from string import Template
import pickle

from parser.grammar import Grammar
from parser.models import CanonicalCollection, ParseTable
from parser.symbols import *


class Parser(object):
    "${dirty_hack}${actual_data}${dirty_hack}"

    def __init__(self, data=None):
        if data is None:
            if not hasattr(self, "pregenerated"):
                raise Exception("ur using this wrong")
            data = self.pregenerated

        self.data = data
        self.table = data["table"]
        self.productions = data["productions"]

    def write(self, f):
        with open(__file__, "r") as f1:
            template = Template(f1.read())
        with open(os.path.join(os.path.dirname(__file__), "symbols.py"), "r") as f1:
            grammar_source = f1.read()
        symbols = "\n" + "\n".join("    {}".format(line)
                                   for line in grammar_source.split("\n")) + "\n    "
        data = "\n    pregenerated = pickle.loads({})\n    ".format(
            pickle.dumps(self.data))
        source = template.substitute(
            dict(dirty_hack="\"", actual_data=data, symbols=symbols))
        f.write(source)

    def parse(self, lexer, verbose=False):
        stack = [0]
        token = lexer.next()

        shifted_token = None
        while True:
            if token is None:
                raise SyntaxError("unexpected end of input")
            state_n = stack[-1]
            state = self.table.get(state_n)
            column = token.symbol
            if column not in state:
                raise SyntaxError("unexpected token from state {}: {} (column = {})\nexpected: {}".format(
                    state_n, token, column, state.keys()))

            entry = state[column]
            if "/" in entry:
                raise Exception("unresolved conflict")
            if entry[0] == "s":
                stack.append(token.symbol)
                stack.append(int(entry[1:]))
                shifted_token = token
                token = lexer.next()
            elif entry[0] == "r":
                production = self.productions[int(entry[1:])]
                rhs_length = len(production.right)
                if len(production.right) == 1 and isinstance(production.right[0], GEPSILON):
                    # special case
                    next_state = stack[-1]
                    symbol = production.left
                    # stack.append(token.symbol)
                    stack.append(GEPSILON())
                    stack.append(int(self.table[next_state].get(symbol)))
                else:
                    args = []
                    while rhs_length > 0:
                        stack.pop()
                        stack_entry = stack.pop()
                        if not isinstance(stack_entry, GEPSILON):
                            args.insert(0, stack_entry)
                        rhs_length -= 1
                    # reduce_stack_entry = type(repr(production.left), (), dict(args=args))()
                    reduce_stack_entry = deepcopy(production.left)
                    reduce_stack_entry.children = args
                    next_state = stack[-1]
                    stack.append(reduce_stack_entry)
                    symbol = production.left
                    stack.append(int(self.table[next_state].get(symbol)))
            elif entry == "acc":
                stack.pop()
                parsed = stack.pop()
                return parsed
            print("(1)", [x if type(x) is int else (
                type(x).__name__, repr(x)) for x in stack])


"${dirty_hack}"


class ParserGenerator(object):
    def __init__(self, grammar, verbose=False):
        self.grammar = grammar
        self.table = ParseTable(CanonicalCollection(
            grammar), grammar, verbose=verbose)

    def generate(self):
        return dict(
            table=self.table.table,
            tokens=self.grammar.get_tokens(),
            productions=self.grammar.productions,
        )


if __name__ == "__main__":
    pgen()

"${dirty_hack}"
