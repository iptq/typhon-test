#!/usr/bin/python3

from lexer import Lexer

if __name__ == "__main__":
    while True:
        try:
            line = input(">> ")
            for token in Lexer(line):
                print(token)
        except KeyboardInterrupt:
            break
