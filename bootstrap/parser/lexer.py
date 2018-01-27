from tokens import *

alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "012346789"

class Lexer(object):
    def __init__(self, source):
        self.source = source + " "
        self.reset()

    def reset(self):
        self.position = 0
        self.line = 1
        self.queue = []
        self.indents = []
        self._eof = False

    def all(self):
        tokens = []
        t = self.next()
        while t is not None:
            tokens.append(t)
            t = self.next()

        self.reset()
        return tokens

    @property
    def eof(self):
        if not self._eof:
            while self.indents:
                self.indents.pop()
                return TDEDENT()
            self._eof = True
            return TEOF()
        return None

    def peek(self, offset=0):
        return self.source[self.position + offset]

    def peek_while(self, f):
        offset = 0
        c = self.peek(offset)
        while f(c) and self.position + offset < len(self.source) - 1:
            offset += 1
            c = self.peek(offset)
        return self.source[self.position:self.position + offset]

    def skip_whitespace(self):
        c = self.peek()
        while c in " \t":
            self.position += 1
            c = self.peek()

    def read_comments(self):
        comment = self.peek_while(lambda c: c != "\n")
        self.position += len(comment) + 1
        return comment

    def read_indents(self):
        curr_indent = self.peek_while(lambda c: c in " \t")
        curr_stack_len = 0
        dedented = False
        for ind, indent in enumerate(self.indents):
            substr = curr_indent[curr_stack_len:curr_stack_len + len(indent)]
            if substr == indent:
                curr_stack_len += len(indent)
            else:
                dedented = True
                break
        if dedented:
            if curr_stack_len != len(curr_indent):
                raise Exception("ur indenting is fuckd", self.line)
            for _ in range(ind, len(self.indents)):
                self.queue.insert(0, TDEDENT())
            self.indents = self.indents[ind:]
        else:
            remain = curr_indent[curr_stack_len:]
            if len(remain) > 0:
                self.indents.append(remain)
                self.queue.insert(0, TINDENT())
        self.position += len(curr_indent)
        # print("indent:", repr(curr_indent))

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
            if c not in digits: break # decimals
            self.position += 1
        self.queue.insert(0, TNumber(self.source[start:self.position]))

    def read_ident(self):
        start = self.position
        offset = 0
        while self.position + offset < len(self.source):
            c = self.peek(offset=offset)
            if c not in (alpha + digits + "_"): break
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
            self.read_indents()
        else:
            self.skip_whitespace()

        c1 = self.peek()
        if c1 == "#":
            self.read_comments()
            return self.next()
        elif c1 == '"' or c1 == "'":
            self.read_string(c1)
        elif c1 in digits:
            self.read_number()
        elif c1 in alpha + "_":
            self.read_ident()
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
                if c1 in "\\|/{}[]()=:;.,+-*%$#@!^&":
                    found = True
                    self.queue.insert(0, TSymbol(c1))
                    self.position += 1
        
        if self.queue:
            return self.queue.pop()
        elif self.position >= len(self.source) - 1:
            return self.eof
        return self.next()