import ast
from copy import deepcopy

from .symbols import *

def flatten(node, nonterminals):
    def rec_flatten(items, front):
        current = []
        for node in items:
            if isinstance(node, ast.BinOp):
                if isinstance(node.op, ast.Add):
                    left = rec_flatten([node.left], deepcopy(front))
                    right = rec_flatten([node.right], deepcopy(front))
                    for sym1 in left:
                        for sym2 in right:
                            full = deepcopy(front)
                            full.extend(sym1 + sym2)
                            current.append(full)
            elif isinstance(node, ast.Set):
                current.append(None)
            elif isinstance(node, ast.List):
                # syntactic sugar for EMPTY, {b}
                flat = flatten(ast.Tuple([ast.Name("EMPTY", node.ctx), ast.Set(node.elts)], node.ctx), front)
                current.append(flat)
            elif isinstance(node, ast.Name):
                if node.id == "IDENT":
                    obj = GIdent()
                elif node.id == "NUMBER":
                    obj = GNum()
                elif node.id == "STRING":
                    obj = GStr()
                elif node.id == "EMPTY":
                    obj = GEPSILON()
                elif node.id == "EOF":
                    obj = GEOF()
                elif node.id == "NEWLINE":
                    obj = GNEWLINE()
                elif node.id == "INDENT":
                    obj = GINDENT()
                elif node.id == "DEDENT":
                    obj = GDEDENT()
                elif node.id in nonterminals:
                    obj = GNT(node.id)
                else:
                    raise NotImplementedError("{} not implemented".format(node.id))
                front.append(obj)
                current.append(deepcopy(front))
            elif isinstance(node, ast.Str):
                front.append(GLiteral(node.s))
                current.append(deepcopy(front))
            elif isinstance(node, ast.Tuple):
                for element in node.elts:
                    flat = rec_flatten([element], deepcopy(front))
                    for sym in flat:
                        current.append(sym)
            else:
                raise NotImplementedError(type(node))
            return current
    return rec_flatten([node], [])