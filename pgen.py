def generate_parser():
    " Generate a parser. "

    from tree import Node
    nodetypes = Node.__subclasses__()
    for nodetype in nodetypes:
        assert nodetype.pattern

    return 1
