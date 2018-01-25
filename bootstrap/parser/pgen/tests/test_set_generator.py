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
            assert sg.first_of(GLiteral('a')) == OrderedSet([GLiteral('a')])
            assert sg.first_of(GLiteral('b')) == OrderedSet([GLiteral('b')])

        def test_rhs(self):
            data = """
S = A + B + 'c', D
A = 'a', EMPTY
B = 'b', EMPTY
D = 'd', EMPTY
""".strip()
            grammar = Grammar.from_data(data)
            sg = SetGenerator(grammar)
            assert sg.first_of_rhs(grammar.productions[1].right) == \
                OrderedSet([GLiteral('a'), GLiteral('b'), GLiteral('c')])
            assert sg.first_of_rhs(grammar.productions[2].right) == \
                OrderedSet([GLiteral('d'), GEPSILON()])

        def test_all_first_sets(self):
            data = """
S = A + B + 'c', D
A = 'a', EMPTY
B = 'b', EMPTY
D = 'd', EMPTY
""".strip()
            grammar = Grammar.from_data(data)
            sg = SetGenerator(grammar)
            assert sg.get_first_sets() == dict([
                ("$accept", OrderedSet([GLiteral('a'), GLiteral('b'), GLiteral('c'), GLiteral('d'), GEPSILON()])),
                ("S", OrderedSet([GLiteral('a'), GLiteral('b'), GLiteral('c'), GLiteral('d'), GEPSILON()])),
                ("A", OrderedSet([GLiteral('a'), GEPSILON()])),
                ("B", OrderedSet([GLiteral('b'), GEPSILON()])),
                ("D", OrderedSet([GLiteral('d'), GEPSILON()])),
            ])

    class TestFollowSets(object):
        def test_start_eof(self):
            sg = SetGenerator(Grammar.from_data("S = 'a'"))
            assert sg.follow_of(GNT('S')) == OrderedSet([GEOF()])

        def test_single_symbol(self):
            data = """
S = A + B + 'c'
A = B + 'a'
B = 'b', EMPTY
""".strip()
            grammar = Grammar.from_data(data)
            sg = SetGenerator(grammar)
            assert sg.follow_of(GNT('S')) == OrderedSet([GEOF()])
            assert sg.follow_of(GNT('A')) == OrderedSet([GLiteral('b'), GLiteral('c')])
            assert sg.follow_of(GNT('A')) == sg.first_of_rhs(grammar.productions[1].right[1:])

        def test_several_symbols(self):
            data = """
S = A + B + A + 'c'
A = 'a'
B = 'b', EMPTY
""".strip()
            grammar = Grammar.from_data(data)
            sg = SetGenerator(grammar)
            rhs = grammar.productions[1].right
            assert sg.follow_of(GNT('S')) == OrderedSet([GEOF()])
            assert sg.follow_of(GNT('A')) == OrderedSet([GLiteral('a'), GLiteral('b'), GLiteral('c')])
            assert sg.follow_of(GNT('A')) == sg.first_of_rhs(rhs[1:]).union(sg.first_of_rhs(rhs[3:]))

        def test_rhs_eliminated_follow_lhs(self):
            data = """
S = A + B + C
A = 'a'
B = 'b', EMPTY
C = 'c', EMPTY
""".strip()
            sg = SetGenerator(Grammar.from_data(data))
            assert sg.follow_of(GNT('S')) == OrderedSet([GEOF()])
            assert sg.follow_of(GNT('A')) == OrderedSet([GLiteral('b'), GLiteral('c'), GEOF()])
