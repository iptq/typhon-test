import sys

from bootstrap.parser import parse

if __name__ == "__main__":
    # what am i compiling
    target = sys.argv[1]

    # read the file
    with open(target) as f:
        data = f.read()

    # parse ast
    tree = parse(data)
