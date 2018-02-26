from tokens import *
class TokenType(object):
    def __init__(self, name):
        self.name = name

class Node(object):
    def __init__(self):
        self.children = []

    def pretty(self, depth=0):
        s = ["  " * depth + repr(self)]
        for child in self.children:
            s.extend(child.pretty(depth + 1))
        return "\n".join(s)


T_DEDENT = TokenType("Dedent")
T_DELIMITER = TokenType("Delimiter")
T_IDENT = TokenType("Ident")
T_INDENT = TokenType("Indent")
T_INTEGER = TokenType("Integer")
T_KEYWORD = TokenType("Keyword")
T_OPERATOR = TokenType("Operator")
T_STRING = TokenType("String")

class Expression(Node):
    pass

class Literal(Expression):
    pass
