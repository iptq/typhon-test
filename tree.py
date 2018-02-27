from tokens import *

types = set()

class NodeMeta(type):
    def __new__(cls, name, bases, namespace):
        c = type.__new__(cls, name, bases, dict(namespace))
        if name != "Node":
            types.add(c)
        return c

class Node(metaclass=NodeMeta):
    def __init__(self):
        self.children = []

    def pretty(self, depth=0):
        s = ["  " * depth + repr(self)]
        for child in self.children:
            s.extend(child.pretty(depth + 1))
        return "\n".join(s)

class Expression(Node):
    "Literal | BinOp"

class BinOp(Node):
    "Expression + T_OPERATOR + Expression"

class Literal(Expression):
    "T_INTEGER | T_STRING"
