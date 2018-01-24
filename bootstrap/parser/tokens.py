class Token(object): pass

class TNEWLINE(Token):
    def __repr__(self):
        return "newline"

class TEOF(Token):
    def __repr__(self):
        return "eof"

class TSymbol(Token):
    def __init__(self, char):
        self.char = char
    def __repr__(self):
        return "sym('{}')".format(self.char)

class TKeyword(Token):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return "key('{}')".format(self.name)

class TString(Token):
    def __init__(self, string):
        self.string = string
    def __repr__(self):
        return "str({})".format(repr(self.string))

class TNumber(Token):
    def __init__(self, number):
        self.number = number
    def __repr__(self):
        return "num({})".format(repr(self.number))