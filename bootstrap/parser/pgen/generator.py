from collection import CanonicalCollection
from set_generator import SetGenerator
from table import ParseTable

class ParserGenerator(object):
    def __init__(self, grammar, output_file):
        self.grammar = grammar
        self.output_file = output_file
        self.output_data = ""

        generator = SetGenerator(self.grammar)
        print("Follow Set")
        for key, value in generator.build_set(generator.follow_of).items():
            print(" ", key, list(map(lambda x: x.key, value)))

        self.table = ParseTable(CanonicalCollection(grammar), grammar)

    def generate(self):
        with open(self.output_file, "w") as f:
            f.write(self.output_data)
        print("success")