#!/usr/bin/python3

from lexer import Lexer
from pgen import generate_parser

if __name__ == "__main__":
    p = generate_parser()
    while True:
        try:
            line = input(">> ")
            tokens = list(Lexer(line))
            for token in tokens:
                print(token)
        except KeyboardInterrupt:
            break
