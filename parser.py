class Parser(object):
    def __init__(self, table, productions):
        self.table = table
        self.productions = productions

    def parse(self, lexer):
        stack = [0]
        token = next(lexer)
        print("oh boy")
