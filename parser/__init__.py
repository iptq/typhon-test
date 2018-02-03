import os


def parsestring(source, verbose=False):
    from parser.generated_parser import Parser as GeneratedParser
    from parser.lexer import Lexer

    if verbose:
        print("TOKENS")
        lexer = Lexer(source)
        for token in lexer.all():
            print(token)

    lexer = Lexer(source)
    parser = GeneratedParser()
    return parser.parse(lexer, verbose=verbose)


def pgen(verbose=False):
    from parser.grammar import Grammar
    from parser.parse import Parser, ParserGenerator

    current_dir = os.path.dirname(__file__)
    grammar_file = os.path.join(current_dir, "Grammar")
    output_file = os.path.join(current_dir, "generated_parser.py")

    grammar = Grammar.from_file(grammar_file, verbose=verbose)
    generator = ParserGenerator(grammar, verbose=verbose)

    parser = Parser(generator.generate())
    with open(output_file, "w") as f:
        parser.write(f)
        f.close()
