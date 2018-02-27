from constants import *
from tokens import *

T_EXPR = TokenType("Expr")
T_LITERAL = TokenType("Literal")
T_IDENT = TokenType("Ident")

class RuleParser(object):
    @classmethod
    def parse(cls, src):
        p = cls(src)
        return p.parse_expr()

    def __init__(self, src):
        self.src = src
        self.line = 1
        self.col = 0
        self.pos = 0

    def parse_ident(self):
        # read ident
        s = ""
        ch = self.src[self.pos]
        while ch in IDENT_REST:
            s += ch
            self.pos += 1
            ch = self.src[self.pos]
        return Token(T_IDENT, self.line, self.col, len(s), [s])

    def skip_whitespace(self):
        ch = self.src[self.pos]
        of = 0
        while ch in " \t\n":
            # ignore
            if ch in " \t":
                self.col += 1
            else:
                self.line += 1
                col = 0
            self.pos += 1
            of += 1
            ch = self.src[self.pos]
        return of

    def parse_expr(self):
        self.skip_whitespace()
        ch = self.src[self.pos]
        tok = None
        if ch in IDENT_FIRST:
            tok = self.parse_ident()
        elif ch == "(":
            self.col += 1
            self.pos += 1
            tok = self.parse_expr()
        ftok = Token(T_EXPR, self.line, self.col, 0, [tok])
        return ftok

class Production(object):
    def __init__(self, left, right):
        self.left = left
        self.right = right
