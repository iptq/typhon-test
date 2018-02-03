colors = None


def color(*args, **kwargs):
    global colors
    if colors is None:
        import colors
    return colors.color(*args, **kwargs)
