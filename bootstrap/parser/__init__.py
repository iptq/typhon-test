import sys
import os
current_dir = os.path.realpath(os.path.dirname(__file__))
sys.path.append(current_dir)

def parse(source):
    from .parser import parse_from_tokens
    from .lexer import Lexer

    print("TOKENS")
    lexer = Lexer(source)
    for token in lexer.all():
        print(token)

    lexer = Lexer(source)
    return parse_from_tokens(lexer)
