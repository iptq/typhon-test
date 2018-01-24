from collection import CanonicalCollection
from table import ParseTable

class ParserGenerator(object):
    def __init__(self, grammar, output_file):
        self.grammar = grammar
        self.output_file = output_file
        self.output_data = ""

        self.table = ParseTable(CanonicalCollection(grammar), grammar)

    def generate(self):
        with open(self.output_file, "w") as f:
            f.write(self.output_data)
        print("success")