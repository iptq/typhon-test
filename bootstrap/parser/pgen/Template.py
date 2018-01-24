import sys
import os
sys.path.append(os.path.join(os.path.realpath(os.path.dirname(__file__)), "pgen"))

import pickle
from tokens import *

table = pickle.loads(${table})
productions = pickle.loads(${productions})

def get_column(token):
    if type(token) is TSymbol:
        return token.char
    elif type(token) is TString:
        return "Str"
    elif type(token) is TNumber:
        return "Num"
    elif type(token) is TEOF:
        return "EOF"

def parse_from_tokens(lexer):
    stack = [0]
    token = lexer.next()

    shifted_token = None
    while True:
        if token is None:
            raise Exception("unexpected end of input")
        if type(token) is TNEWLINE:
            token = lexer.next()
            continue
        print(token)
        state_n = stack[-1]
        column = get_column(token)
        state = table.get(state_n)
        if column not in state:
            print(state.keys())
            raise Exception("unexpected token {} (column = {})".format(token, column))
        
        entry = state[column]
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
            reduce_stack_entry = type(production.left, (), dict(args=args))
            next_state = stack[-1]
            symbol_to_reduce_with = production.left
            stack.append(reduce_stack_entry)
            stack.append(int(table[next_state][symbol_to_reduce_with]))
        elif entry == "acc":
            stack.pop()
            parsed = stack.pop()
            return parsed
        print(stack)