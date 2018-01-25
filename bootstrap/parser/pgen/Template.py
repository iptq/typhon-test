import sys
import os
sys.path.append(os.path.join(os.path.realpath(os.path.dirname(__file__)), "pgen"))

import pickle
from .tokens import *
from grammar.symbols import *

table = pickle.loads(${table})
productions = pickle.loads(${productions})
tokens = pickle.loads(${tokens})

def parse_from_tokens(lexer, verbose=False):
    stack = [0]
    token = lexer.next()

    shifted_token = None
    while True:
        if token is None:
            raise Exception("unexpected end of input")
        state_n = stack[-1]
        state = table.get(state_n)
        column = token.symbol
        if column not in state:
            print(state.keys())
            raise Exception("unexpected token from state {}: {} (column = {})".format(state_n, token, column))
        
        entry = state[column]
        if "/" in entry:
            raise Exception("unresolved conflict")
        if entry[0] == "s":
            stack.append(token)
            stack.append(int(entry[1:]))
            shifted_token = token
            token = lexer.next()
        elif entry[0] == "r":
            production = productions[int(entry[1:])]
            rhs_length = len(production.right)
            args = []
            while rhs_length > 0:
                stack.pop()
                stack_entry = stack.pop()
                args.append(stack_entry)
                rhs_length -= 1
            reduce_stack_entry = type(production.left, (), dict(args=args))()
            stack.append(reduce_stack_entry)
            next_state = stack[-1]
            symbol = production.left
            print(next_state, symbol)
            stack.append(int(table[next_state].get(symbol)))
        elif entry == "acc":
            stack.pop()
            parsed = stack.pop()
            return parsed
        if verbose:
            print([x if type(x) is int else type(x).__name__ for x in stack])
