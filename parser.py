class Parser(object):
    def __init__(self):
        self.table = dict()

    def parse(self, lexer):
        stack = [0]
        token = next(lexer)
        while True:
            if token is None:
                raise SyntaxError("Unexpected end of input.")
            nstate = stack[-1]
            state = self.table.get(nstate)
            break  # TODO
