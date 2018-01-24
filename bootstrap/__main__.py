def compile(source):
    # step 0: generate parser
    from parser.pgen import pgen
    pgen()
    print("+ generated praser")

    # step 1: parse tokens
    from parser import parse
    print(parse(source))
    print("+ parsed source")

    # step 2: basic semantic analysis
    # ???

    # step 3: ???

if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        data = f.read()
    result = compile(data)
