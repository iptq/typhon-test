# pretty much gonna be a straight port from syntax into whatever the fuck i'm doing here

from collection import CanonicalCollection
from grammar import Grammar
from parser import Parser

def generate_parser(mode):
    " Generate a parser. "

    from tree import Node
    classlist = Node.__subclasses__()
    for nodetype in classlist:
        assert nodetype.pattern
    grammar = Grammar(classlist, mode)
    collection = CanonicalCollection(grammar)
    collection.print()

    table = None

    return Parser(table, grammar.productions)
