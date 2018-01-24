import os
import sys
sys.path.append(os.path.realpath(os.path.dirname(os.path.dirname(__file__))))

from collection import CanonicalCollection
from item import Item, ItemSet
from grammar import Grammar
from orderedset import OrderedSet
from set_generator import SetGenerator
from grammar.symbols import *

grammar = Grammar.from_data("""
Expression = Number, Add, Sub
Number = NUMBER
Add = Expression + "+" + Expression
Sub = Expression + "-" + Expression
""")
collection = CanonicalCollection(grammar)
set_generator = SetGenerator(grammar)

root_item = Item(grammar.augmented, 0, grammar, collection, set_generator, OrderedSet([GEOF()]))
base_item = Item(grammar.productions[1], 0, grammar, collection, set_generator, OrderedSet([GEOF(), GLiteral("+"), GLiteral("-")]))
advance_item = base_item.advance()

class TestLRItem(object):
    def test_production(self):
        assert root_item.production == grammar.augmented
        assert base_item.production == grammar.productions[1]
        assert advance_item.production == grammar.productions[1]

    def test_dot_position(self):
        assert root_item.dot == 0
        assert base_item.dot == 0
        assert advance_item.dot == 1

    def test_advance(self):
        assert advance_item.production == base_item.production
        assert advance_item.dot == base_item.dot + 1
        assert advance_item.lookahead_set == base_item.lookahead_set

    def test_key(self):
        assert root_item.key == "0|0|$"
        assert base_item.key == "1|0|+,-,$"
        assert advance_item.key == "1|1|+,-,$"

    def test_lr0_key(self):
        assert root_item.lr0_key == "0|0"
        assert base_item.lr0_key == "1|0"
        assert advance_item.lr0_key == "1|1"

    def test_set_key(self):
        items = ItemSet([base_item, advance_item])
        keys = [base_item.key, advance_item.key]
        assert items.key == "|".join(keys)

    def test_set_lr0_key(self):
        other_base_item = Item(base_item.production, 0, grammar, collection, set_generator, OrderedSet([GLiteral("%")]))
        items = ItemSet([base_item, other_base_item, advance_item])
        keys = [base_item.lr0_key, advance_item.lr0_key]
        assert items.lr0_key == "|".join(keys)