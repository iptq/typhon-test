class TokenType(object):
    def __init__(self, name):
        self.name = name

    def __or__(self, other):
        return self

class Token(object):
    def __init__(self, type, line, col, length, args=None):
        assert isinstance(type, TokenType)
        if args is None:
            args = []
        self.type = type
        self.line = line
        self.col = col
        self.length = length
        self.args = args

    def __repr__(self):
        return "<{}({},{}:{}){}>".format(self.type.name, self.line, self.col, self.length, self.args)


T_DEDENT = TokenType("Dedent")
T_DELIMITER = TokenType("Delimiter")
T_IDENT = TokenType("Ident")
T_INDENT = TokenType("Indent")
T_INTEGER = TokenType("Integer")
T_KEYWORD = TokenType("Keyword")
T_OPERATOR = TokenType("Operator")
T_STRING = TokenType("String")
