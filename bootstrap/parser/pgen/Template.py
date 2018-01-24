import pickle
from tokens import *

table = pickle.loads(${table})

def get_column(token):
    if type(token) is TSymbol:
        return token.char
    elif type(token) is TString:
        return "Str"

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
        state = stack[-1]
        column = get_column(token)
        state = table.get(state)
        if column not in state:
            print(state.keys())
            raise Exception("unexpected token {} (column = {})".format(token, column))
        
        entry = state[column]
        if entry[0] == "s":
            stack.append(token)
            stack.append(int(entry[1:]))
            shifted_token = token
            token = lexer.next()
        print(stack)