def compile(source):
    # step 0: generate parser
    from parser.pgen import pgen
    pgen(verbose=True)
    print("+ generated praser")

    # step 1: parse tokens
    from parser import parse
    syntree = parse(source, verbose=True)
    print("+ parsed source")

    # step 2: build data model
    from datamodel import build
    print(build(syntree))
    print("+ built a data model")

    # step 3: ???

if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        data = f.read()
    result = compile(data)
