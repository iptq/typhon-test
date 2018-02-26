#!/usr/bin/python3

import os
import sys

from lexer import Lexer

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        contents = f.read()
    l = Lexer(contents)
    for token in l:
        print(token)
