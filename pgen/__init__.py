from tree import Node, types
from pgen.production import RuleParser

def aggregate_productions():
    productions = []
    for ntype in types:
        print(ntype)
        t = RuleParser.parse(ntype.__doc__)
        print(repr(t))
    return productions

def generate_parser(mode):
    productions = aggregate_productions()
    return 1
