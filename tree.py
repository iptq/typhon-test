class Node(object):
    pattern = None

    def __init__(self):
        self.children = []

    def pretty(self, depth=0):
        s = ["  " * depth + repr(self)]
        for child in self.children:
            s.extend(child.pretty(depth + 1))
        return "\n".join(s)

class Expression(Node):
    " Anything that produces a value. "
    pattern = "shiet"

class Literal(Expression):
    " Any literal. "
    pattern = "shiet"
