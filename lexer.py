# ref: https://docs.python.org/3/reference/lexical_analysis.html

from constants import *
from tokens import *

def preprocess(text):
    text = text.replace("\r\n", "\n")  # crlf -> lf
    text = text + "\n"  # tack on a new line to get dedents
    return text

class Lexer(object):
    def __init__(self, source):
        self.source = preprocess(source)
        self.istack = [0]  # indent stack
        self.pos = 0
        self.line = 0
        self.col = 0
        self.newline = True
        self.q = []

    def __iter__(self):
        return self

    def peek(self, offset=0, count=1):
        start = min(len(self.source), self.pos + offset)
        end = min(len(self.source), self.pos + offset + count)
        return self.source[start:end]

    def peek_while(self, fn):
        l = 0
        while fn(self.peek(offset=l)):
            l += 1
        return self.peek(count=l)

    def read_comment(self):
        self.pos += 1
        comment = self.peek_while(lambda c: c != "\n")
        self.pos += len(comment)
        # don't worry about col i guess
        return next(self)

    def read_ident(self):
        ident = self.peek_while(lambda c: c in IDENT_REST)
        type = T_KEYWORD if ident in KEYWORDS else T_IDENT
        return Token(type, self.line, self.col, len(ident), [ident])

    def read_number(self):
        n = self.peek_while(lambda c: c in DIGIT)  # TODO: float
        return Token(T_INTEGER, self.line, self.col, len(n), [n])

    def read_string(self, quote):
        self.pos += len(quote)
        s = self.peek_while(lambda c: c != quote)  # TODO: escaped characters
        self.pos += len(quote)
        return Token(T_STRING, self.line, self.col, len(s), [s])

    def try_read_symbol(self, pattern):
        if pattern in OPERATORS:
            return Token(T_OPERATOR, self.line, self.col, len(pattern), [pattern])
        if pattern in DELIMITERS:
            return Token(T_DELIMITER, self.line, self.col, len(pattern), [pattern])
        return None

    def __next__(self):
        # this is so i can push multiple tokens to return at a time
        if self.q:
            return self.q.pop()

        if self.newline == True:
            # oh boy
            # ref: https://docs.python.org/3/reference/lexical_analysis.html#indentation
            # count the whitespace
            whitespace = self.peek_while(lambda c: c == " ")  # spaces masterrace
            wlen = len(whitespace)
            if wlen == self.istack[-1]:
                # we're at the same indentation level
                self.newline = False
                self.pos += self.istack[-1]
                self.col += self.istack[-1]
                return next(self)
            elif wlen > self.istack[-1]:
                self.istack.append(wlen)
                tok = Token(T_INDENT, self.line, self.col, wlen - self.istack[-1])
                self.pos += tok.length
                self.col += tok.length
                return tok
            elif wlen < self.istack[-1]:
                print(wlen, self.istack)
                if wlen in self.istack:
                    while wlen != self.istack[-1] and self.istack[-1] != 0:
                        n = self.istack.pop()
                        amt = n - self.istack[-1]
                        self.q.insert(0, Token(T_DEDENT, self.line, self.col, 0, [amt]))
                        wlen -= amt
                    return next(self)
                else:
                    raise SyntaxError("Unexpected indentation.")
        ch = self.peek()
        if not ch:
            raise StopIteration()
        # print("peeked: '{}'".format(ch))
        if ch == "\n":
            self.newline = True
            self.pos += 1
            self.line += 1
            self.col = 0
            return next(self)
        elif ch == " " or ch == "\t":
            # ignore whitespace
            self.pos += 1
            self.col += 1
            return next(self)
        elif ch == "#":
            return self.read_comment()
        elif ch == "'" or ch == "\"":
            tok = self.read_string(ch)
            self.pos += tok.length
            self.col += tok.length
            return tok
        elif ch in DIGIT:
            tok = self.read_number()
            self.pos += tok.length
            self.col += tok.length
            return tok
        elif ch in IDENT_FIRST:
            tok = self.read_ident()
            self.pos += tok.length
            self.col += tok.length
            return tok
        ch2 = self.peek(offset=1)
        ch3 = self.peek(offset=2)
        if ch3:
            tok = self.try_read_symbol(ch + ch2 + ch3)
            if tok is not None:
                self.pos += tok.length
                self.col += tok.length
                return tok
        if ch2:
            tok = self.try_read_symbol(ch + ch2)
            if tok is not None:
                self.pos += tok.length
                self.col += tok.length
                return tok
        tok = self.try_read_symbol(ch)
        if tok is not None:
            self.pos += tok.length
            self.col += tok.length
            return tok
        raise StopIteration()
