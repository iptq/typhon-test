from parser import parse_from_tokens
from lexer import Lexer

def parse(source):
    lexer = Lexer(source)
    for token in lexer.all():
        print(token)

    lexer = Lexer(source)
    return parse_from_tokens(lexer)

if __name__ == "__main__":
    import sys
    filename = sys.argv[1]
    with open(filename, "r") as f:
        source = f.read()
    print(parse(source))
