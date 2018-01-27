# the version of the compiler written in Real python

import colors

def compile(source):
    # step 0: generate parser
    from parser.pgen import pgen
    pgen(verbose=True)
    print(colors.color("+ generated praser", fg_green=True))

    # step 1: parse tokens
    from parser import parse
    syntree = parse(source, verbose=True)
    print(colors.color("+ parsed source", fg_green=True))

    # step 2: build symbol table
    from datamodel import build
    print(build(syntree))
    print(colors.color("+ built a symbol table", fg_green=True))

    # step 3: ???

if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        data = f.read()
    result = compile(data)
