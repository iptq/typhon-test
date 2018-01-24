class OrderedSet(object):
    def __init__(self):
        self.elements = []
        self.map = dict()

    def add(self, item):
        if item.key in self.map:
            return
        self.map[item.key] = len(self.elements)
        self.elements.append(item)

    def __contains__(self, item):
        return item.key in self.map

    def __len__(self):
        return len(self.elements)

    def __getitem__(self, key):
        if type(key) is int:
            return self.elements[key]
        elif type(key) is str:
            return self.elements[self.map[key]]

    def __iter__(self):
        for item in self.elements:
            yield item

    def __repr__(self):
        return "[{}]".format(", ".join([repr(item) for item in self.elements]))