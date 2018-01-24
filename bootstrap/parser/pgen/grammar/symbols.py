class GrammarSymbol(object):
    # base class    
    @property
    def key(self):
        return self
    def __hash__(self):
        return hash(self.key)
    def __repr__(self):
        return self.key
    def __eq__(self, other):
        return hash(self) == hash(other)

class GEOF(object):
    @property
    def key(self):
        return "EOF"

class GIdent(GrammarSymbol):
    terminal = True
    def __repr__(self):
        return "Id"

class GStr(GrammarSymbol):
    terminal = True
    @property
    def key(self):
        return "Str"

class GNum(GrammarSymbol):
    terminal = True
    @property
    def key(self):
        return "Num"

class GLiteral(GrammarSymbol):
    terminal = True
    def __init__(self, string):
        self.string = string
    @property
    def key(self):
        return self.string

class GNT(GrammarSymbol):
    terminal = False
    def __init__(self, name):
        self.name = name
    @property
    def key(self):
        return self.name
