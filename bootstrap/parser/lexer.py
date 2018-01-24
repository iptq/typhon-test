from tokens import *

alpha = "abcdefghijklmnopqrstuvwxyz"

class Lexer(object):
    def __init__(self, source):
        self.source = source
        self.position = 0
        self.line = 1
        self.queue = []
        self._eof = False

    def all(self):
        tokens = []
        t = self.next()
        while t is not None:
            tokens.append(t)
            t = self.next()
        return tokens

    @property
    def eof(self):
        if not self._eof:
            self._eof = True
            return TEOF()
        return None

    def peek(self, offset=0):
        return self.source[self.position + offset]

    def skip_whitespace(self):
        c = self.peek()
        while c in " \t":
            self.position += 1
            c = self.peek()

    def read_string(self, quote):
        self.position += len(quote)
        start = self.position
        offset = 0
        while self.position + offset < len(self.source):
            c = self.peek(offset=offset)
            if c == quote:
                # escaping
                break
            self.position += 1
        self.queue.insert(0, TString(self.source[start:self.position]))
        self.position += len(quote)

    def read_number(self):
        start = self.position
        offset = 0
        while self.position + offset < len(self.source):
            c = self.peek(offset=offset)
            if c not in "0123456789": break # decimals
            self.position += 1
        self.queue.insert(0, TNumber(self.source[start:self.position]))

    def read_keyword(self):
        start = self.position
        offset = 0
        while self.position + offset < len(self.source):
            c = self.peek(offset=offset)
            if c not in alpha: break
            self.position += 1
        self.queue.insert(0, TIdent(self.source[start:self.position]))

    def next(self):
        if self.queue:
            return self.queue.pop()
        if self.position >= len(self.source) - 1:
            return self.eof

        if self.peek() == "\n":
            self.position += 1
            self.line += 1
            self.queue.insert(0, TNEWLINE())

            # read indents
        else:
            self.skip_whitespace()

        c1 = self.peek()
        if c1 == '"' or c1 == "'":
            self.read_string(c1)
        elif c1 in "012346789":
            self.read_number()
        elif c1 in alpha:
            self.read_keyword()
        else:
            found = False
            if self.position < len(self.source) - 1:
                c2 = self.peek(offset=1)
                double = c1 + c2
                if double in ["=="]:
                    found = True
                    self.queue.insert(0, TSymbol(double))
                    self.position += 2
            if not found:
                if c1 in "{}[]()=:;.,+-*/":
                    found = True
                    self.queue.insert(0, TSymbol(c1))
                    self.position += 1
        
        if self.queue:
            return self.queue.pop()
        else:
            return self.eof