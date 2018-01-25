import sys
import os
current_dir = os.path.realpath(os.path.dirname(__file__))
sys.path.append(current_dir)

def parse(source, verbose=False):
    from .parser import parse_from_tokens
    from .lexer import Lexer

    if verbose:
        print("TOKENS")
        lexer = Lexer(source)
        for token in lexer.all():
            print(token)

    lexer = Lexer(source)
    return parse_from_tokens(lexer, verbose=verbose)
