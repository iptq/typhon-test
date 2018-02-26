class TokenType(object):
    def __init__(self, name):
        self.name = name


T_DEDENT = TokenType("Dedent")
T_DELIMITER = TokenType("Delimiter")
T_IDENT = TokenType("Ident")
T_INDENT = TokenType("Indent")
T_INTEGER = TokenType("Integer")
T_KEYWORD = TokenType("Keyword")
T_OPERATOR = TokenType("Operator")
T_STRING = TokenType("String")
