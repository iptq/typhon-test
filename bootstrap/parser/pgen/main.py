# pretty much direct port of https://github.com/DmitrySoshnikov/syntax

import os

from generator import ParserGenerator
from grammar import Grammar

if __name__ == "__main__":
    current_dir = os.path.realpath(os.path.dirname(__file__))
    grammar_file = os.path.join(current_dir, "Grammar")
    output_file = os.path.join(current_dir, "parser.py")

    grammar = Grammar.from_file(grammar_file)
    generator = ParserGenerator(grammar, output_file)

    generator.generate()
