# import sys
# import os
# sys.path.append(os.path.join(os.path.realpath(os.path.dirname(os.path.dirname(__file__))), "parser"))

# import parser
from .visitor import Visitor

def build(syntree):
    v = Visitor(syntree)
    # return v.visit(v.root)
