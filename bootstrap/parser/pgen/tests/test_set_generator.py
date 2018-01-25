import os
import sys
sys.path.append(os.path.realpath(os.path.dirname(os.path.dirname(__file__))))

from set_generator import SetGenerator
from grammar import Grammar
from grammar.symbols import *
from orderedset import OrderedSet

class TestSetGenerator(object):
    class TestFirstSets(object):
        def test_direct(self):
            sg = SetGenerator(Grammar.from_data("S = 'a', 'b'"))
            assert sg.first_of(GNT('S')) == OrderedSet([GLiteral('a'), GLiteral('b')])
            assert sg.first_of(GLiteral('a')) == OrderedSet([GLiteral('a')])
            assert sg.first_of(GLiteral('b')) == OrderedSet([GLiteral('b')])

        def test_indirect(self):
            sg = SetGenerator(Grammar.from_data("S = 'a', B\nB = 'b'"))
            assert sg.first_of(GNT('S')) == OrderedSet([GLiteral('a'), GLiteral('b')])
            assert sg.first_of(GNT('B')) == OrderedSet([GLiteral('b')])
            assert sg.first_of(GLiteral('a')) == OrderedSet([GLiteral('a')])
            assert sg.first_of(GLiteral('b')) == OrderedSet([GLiteral('b')])

        def test_epsilon(self):
            sg = SetGenerator(Grammar.from_data("S = 'a', B + 'c'\nB = 'b', EMPTY"))
            assert sg.first_of(GNT('S')) == OrderedSet([GLiteral('a'), GLiteral('b'), GLiteral('c')])
            assert sg.first_of(GNT('B')) == OrderedSet([GLiteral('b'), GEPSILON()])

    class TestFollowSets(object):
        def test_start_eof(self):
            sg = SetGenerator(Grammar.from_data("S = 'a'"))
            assert sg.follow_of(GNT('S')) == OrderedSet([GEOF()])