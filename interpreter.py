#!/usr/bin/python3

from constants import *
from lexer import Lexer
from pgen import generate_parser

if __name__ == "__main__":
    print("generating parser..", end="\r")
    parser = generate_parser(MODE_INTERPRET)
    print("generating parser.. done")
    while True:
        try:
            line = input(">> ")
            tokens = list(Lexer(line))
            for token in tokens:
                print(token)
            parser.parse(Lexer(line))
        except EOFError:
            break
        except KeyboardInterrupt:
            break
