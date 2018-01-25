# pretty much direct port of https://github.com/DmitrySoshnikov/syntax

import sys
import os
current_dir = os.path.realpath(os.path.dirname(__file__))
sys.path.append(current_dir)

from generator import ParserGenerator
from grammar import Grammar

def pgen(verbose=False):
    grammar_file = os.path.join(os.path.dirname(current_dir), "Grammar")
    output_file = os.path.join(os.path.dirname(current_dir), "parser.py")

    grammar = Grammar.from_file(grammar_file, verbose=verbose)
    generator = ParserGenerator(grammar, output_file, verbose=verbose)

    generator.generate(verbose=verbose)

if __name__ == "__main__":
    pgen()
