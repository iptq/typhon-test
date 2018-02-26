# from keyword.kwlist
KEYWORDS = ["False", "None", "True", "and", "as", "assert", "break", "class", "continue", "def", "del", "elif", "else", "except", "finally", "for",
            "from", "global", "if", "import", "in", "is", "lambda", "nonlocal", "not", "or", "pass", "raise", "return", "try", "while", "with", "yield"]

alpha_lower = "abcdefghijklmnopqrstuvwxyz"
alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha_all = alpha_lower + alpha_upper

digit = "0123456789"
hexdigit = digit + "abcdef"

ident_first = alpha_all + "_"
ident_rest = ident_first + digit

class Token(object):
    def __init__(self, name, line, col, length, args=None):
        if args is None:
            args = []
        self.name = name
        self.line = line
        self.col = col
        self.length = length
        self.args = args

    def __str__(self):
        return "<{}({},{}:{}){}>".format(self.name, self.line, self.col, self.length, self.args)

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

    def __iter__(self):
        return self

    def peek(self, offset=0, count=1):
        return self.source[self.pos + offset:self.pos + offset + count]

    def peek_while(self, fn):
        l = 0
        while fn(self.source[self.pos + l]):
            l += 1
        return self.source[self.pos:self.pos + l]

    def read_ident(self):
        ident = self.peek_while(lambda c: c in ident_rest)
        name = "Keyword" if ident in KEYWORDS else "Ident"
        return Token(name, self.line, self.col, len(ident), [ident])

    def __next__(self):
        if self.newline == True:
            # oh boy
            # ref: https://docs.python.org/3/reference/lexical_analysis.html#indentation
            # count the whitespace
            whitespace = self.peek_while(lambda c: c in " \t")
            if len(whitespace) not in self.istack:
                raise SyntaxError("Unexpected indentation.")
            wlen = len(whitespace)
            if wlen == self.istack[-1]:
                # we're at the same indentation level
                self.newline = False
                self.pos += self.istack[-1]
                self.col += self.istack[-1]
                return next(self)
        ch = self.peek()
        print("peeked: '{}'".format(ch))
        if ch == "\n":
            self.newline = True
            self.line += 1
            self.col = 0
            return next(self)
        elif ch == " " or ch == "\t":
            # ignore whitespace
            self.pos += 1
            return next(self)
        elif ch in ident_first:
            return self.read_ident()
        raise StopIteration()
