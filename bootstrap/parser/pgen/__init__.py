# pretty much direct port of https://github.com/DmitrySoshnikov/syntax

import sys
import os
current_dir = os.path.realpath(os.path.dirname(__file__))
sys.path.append(current_dir)

from string import Template
import pickle

from generator import ParserGenerator
from grammar import Grammar

def pgen(verbose=False):
    grammar_file = os.path.join(os.path.dirname(current_dir), "Grammar")
    output_file = os.path.join(os.path.dirname(current_dir), "parser.py")
    template_file = os.path.join(current_dir, "Template.py")

    grammar = Grammar.from_file(grammar_file, verbose=verbose)
    generator = ParserGenerator(grammar, verbose=verbose)

    parser_data = generator.generate(verbose=verbose)
    with open(template_file, "r") as f:
        template = Template(f.read())

    pickled_parser_data = dict(map(lambda v: (v[0], pickle.dumps(v[1])), parser_data.items()))
    data = template.substitute(pickled_parser_data)
    with open(output_file, "w") as f:
        f.write(data)
        f.close()

if __name__ == "__main__":
    pgen()
