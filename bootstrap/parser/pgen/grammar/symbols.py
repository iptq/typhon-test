class GrammarSymbol(object):
    # base class
    @property
    def key(self):
        return self
    

class GIdent(GrammarSymbol):
    def __repr__(self):
        return "Id"

class GStr(GrammarSymbol):
    def __repr__(self):
        return "Str"

class GLiteral(GrammarSymbol):
    def __init__(self, string):
        self.string = string
    def __repr__(self):
        return "{}".format(repr(self.string))

class GNT(GrammarSymbol):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return "NT({})".format(self.name)
    @property
    def key(self):
        return self.name
