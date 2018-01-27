# pretty much direct port of https://github.com/DmitrySoshnikov/syntax

import sys
import os
current_dir = os.path.realpath(os.path.dirname(__file__))
sys.path.insert(0, current_dir)

from string import Template
from generator import ParserGenerator
from grammar import Grammar
from pgen.parser import Parser

def pgen(verbose=False):
    grammar_file = os.path.join(os.path.dirname(current_dir), "Grammar")
    output_file = os.path.join(os.path.dirname(current_dir), "generated_parser.py")

    grammar = Grammar.from_file(grammar_file, verbose=verbose)
    generator = ParserGenerator(grammar, verbose=verbose)

    parser = Parser(generator.generate())
    with open(output_file, "w") as f:
        parser.write(f)
        f.close()

if __name__ == "__main__":
    pgen()
