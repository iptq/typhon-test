class GrammarSymbol(object):
    # base class   
    terminal = True
    is_epsilon = False
    @property
    def key(self):
        return self
    def __hash__(self):
        return hash(self.key)
    def __repr__(self):
        return self.key
    def __eq__(self, other):
        return hash(self) == hash(other)

class GEOF(GrammarSymbol):
    @property
    def key(self):
        return "$"

class GEPSILON(GrammarSymbol):
    is_epsilon = True
    @property
    def key(self):
        return "e"

class GNEWLINE(GrammarSymbol):
    @property
    def key(self):
        return "\\n"

class GDEDENT(GrammarSymbol):
    @property
    def key(self):
        return "<--"

class GINDENT(GrammarSymbol):
    @property
    def key(self):
        return "-->"

class GIdent(GrammarSymbol):
    @property
    def key(self):
        return "Id"

class GStr(GrammarSymbol):
    @property
    def key(self):
        return "Str"

class GNum(GrammarSymbol):
    @property
    def key(self):
        return "Num"

class GLiteral(GrammarSymbol):
    def __init__(self, string):
        self.string = string
    @property
    def key(self):
        return repr(self.string)

class GNT(GrammarSymbol):
    terminal = False
    def __init__(self, name):
        self.name = name
    @property
    def key(self):
        return self.name
