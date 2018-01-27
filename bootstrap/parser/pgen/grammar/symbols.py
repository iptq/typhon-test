class GrammarSymbol(object):
    # base class   
    terminal = True
    is_epsilon = False
    def __init__(self):
        self.children = []
    @property
    def key(self):
        return self
    def __hash__(self):
        return hash(self.key)
    def __repr__(self):
        return self.key
    def __eq__(self, other):
        return hash(self) == hash(other)
    def print(self, depth=0):
        print("  " * depth + "{} ({})".format(type(self).__name__, repr(self)))
        for child in self.children:
            child.print(depth + 1)

class GEOF(GrammarSymbol):
    @property
    def key(self):
        return "$"

class GEPSILON(GrammarSymbol):
    is_epsilon = True
    terminal = False
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
        self.children = []
        self.string = string
    @property
    def key(self):
        return repr(self.string)

class GNT(GrammarSymbol):
    terminal = False
    def __init__(self, name):
        self.children = []
        self.name = name
    @property
    def key(self):
        return self.name
