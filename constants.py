# from keyword.kwlist
KEYWORDS = ["False", "None", "True", "and", "as", "assert", "break", "class", "continue", "def", "del", "elif", "else", "except", "finally", "for",
            "from", "global", "if", "import", "in", "is", "lambda", "nonlocal", "not", "or", "pass", "raise", "return", "try", "while", "with", "yield"]
OPERATORS = sorted(["+", "-", "*", "**", "/", "//", "%", "@",
                    "<<", ">>", "&", "|", "^", "~",
                    "<", ">", "<=", ">=", "==", "!="], key=len, reverse=True)
DELIMITERS = sorted(['(', ')', '[', ']', '{', '}',
                     ',', ':', '.', ';', '@', '=', '->',
                     '+=', '-=', '*=', '/=', '//=', '%=', '@=',
                     '&=', '|=', '^=', '>>=', '<<=', '**='], key=len, reverse=True)
SYMBOLS = sorted(OPERATORS + DELIMITERS, key=len, reverse=True)

ALPHA_LOWER = "abcdefghijklmnopqrstuvwxyz"
ALPHA_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHA_ALL = ALPHA_LOWER + ALPHA_UPPER

DIGIT = "0123456789"
HEXDIGIT = DIGIT + "abcdef"

IDENT_FIRST = ALPHA_ALL + "_"
IDENT_REST = IDENT_FIRST + DIGIT
