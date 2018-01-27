import sys
import os
current_dir = os.path.realpath(os.path.dirname(__file__))
sys.path.insert(0, current_dir)

def parse(source, verbose=False):
    from .generated_parser import Parser
    from .lexer import Lexer

    if verbose:
        print("TOKENS")
        lexer = Lexer(source)
        for token in lexer.all():
            print(token)

    lexer = Lexer(source)
    parser = Parser()
    return parser.parse(lexer, verbose=verbose)
