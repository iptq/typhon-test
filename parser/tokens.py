from parser.symbols import *

KEYWORDS = ["def", "hello"]


class Token(object):
    def __repr__(self):
        return self.symbol.key

    @property
    def symbol(self):
        raise NotImplementedError("fuc", type(self).__name__)


class TNEWLINE(Token):
    @property
    def symbol(self):
        return GNEWLINE()


class TINDENT(Token):
    @property
    def symbol(self):
        return GINDENT()


class TDEDENT(Token):
    @property
    def symbol(self):
        return GDEDENT()


class TEOF(Token):
    def __repr__(self):
        return self.symbol.key

    @property
    def symbol(self):
        return GEOF()


class TSymbol(Token):
    def __init__(self, char):
        self.char = char

    def __repr__(self):
        return "'{}'".format(self.char)

    @property
    def symbol(self):
        return GLiteral(self.char)


class TIdent(Token):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "'{}'".format(self.name)

    @property
    def symbol(self):
        if self.name in KEYWORDS:
            return GLiteral(self.name)
        return GIdent()


class TString(Token):
    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return "{}".format(repr(self.string))

    @property
    def symbol(self):
        return GStr()


class TNumber(Token):
    def __init__(self, number):
        self.number = number

    def __repr__(self):
        return "num({})".format(repr(self.number))
