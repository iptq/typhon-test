class GrammarSymbol(object):
    # base class
    pass

class GIdent(object):
    def __repr__(self):
        return "Id"

class GStr(object):
    def __repr__(self):
        return "Str"

class GLiteral(object):
    def __init__(self, string):
        self.string = string
    def __repr__(self):
        return "{}".format(repr(self.string))

class GNT(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return "NT({})".format(self.name)
