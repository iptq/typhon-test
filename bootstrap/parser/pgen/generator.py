import os
from string import Template
import pickle

from collection import CanonicalCollection
from set_generator import SetGenerator
from table import ParseTable

class ParserGenerator(object):
    def __init__(self, grammar, output_file, template_file=None):
        self.grammar = grammar
        self.output_file = output_file
        self.template_file = template_file

        if not self.template_file:
            self.template_file = os.path.join(os.path.realpath(os.path.dirname(__file__)), "Template.py")

        self.table = ParseTable(CanonicalCollection(grammar), grammar)

    def generate(self):
        with open(self.template_file, "r") as f:
            template = Template(f.read())

        output_data = template.substitute(dict(
            table=pickle.dumps(self.table.table),
            tokens=pickle.dumps(self.grammar.get_tokens()),
            productions=pickle.dumps(self.grammar.productions),
        ))

        with open(self.output_file, "w") as f:
            f.write(output_data)
        print("success")