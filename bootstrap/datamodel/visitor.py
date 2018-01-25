from .symboltable import SymbolTable

class Visitor(object):
    def __init__(self, syntree):
        self.root = syntree
        self.table = SymbolTable()

    def visit(self, node):
        node_type = type(node).__name__
        if node_type == "Start":
            # follow it on
            self.visit(node.args[0])
        elif node_type == "CompoundStmt":
            # TODO
            self.visit(node.args[0])
        elif node_type == "FuncDef":
            # TODO
            self.visit(node.args[0])
        elif node_type == "Program":
            # TODO
            self.visit(node.args[0])
        elif node_type == "Stmt":
            # TODO
            self.visit(node.args[0])
        elif node_type == "Suite":
            # nice
            if len(node.args) == 1:
                # it's a SimpleStmt
                pass #TODO
            elif len(node.args) == 4:
                # it's a block
            self.visit(node.args[0])
        elif node_type == "Indent" or node_type == "Dedent":
            # ignore
            pass
        else:
            raise NotImplementedError("haven't visited {} before".format(node_type))
