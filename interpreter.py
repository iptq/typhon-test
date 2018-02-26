#!/usr/bin/python3

# pylint: disable=W0614
from constants import *
from lexer import Lexer
from pgen import generate_parser

if __name__ == "__main__":
    parser = generate_parser(MODE_INTERPRET)
    while True:
        try:
            line = input(">> ")
            tokens = list(Lexer(line))
            for token in tokens:
                print(token)
            parser.parse(Lexer(line))
        except KeyboardInterrupt:
            break
