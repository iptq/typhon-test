class TokenType(object):
    def __init__(self, name):
        self.name = name

    def __or__(self, other):
        return self

class Token(object):
    def __init__(self, type, line, col, length, args=None):
        if args is None:
            args = []
        self.type = type
        self.line = line
        self.col = col
        self.length = length
        self.args = args

    def __repr__(self):
        return "<{}({},{}:{}){}>".format(self.type, self.line, self.col, self.length, self.args)
