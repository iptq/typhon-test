from copy import deepcopy

class OrderedSet(object):
    def __init__(self, iterable=None):
        self.elements = []
        self.map = dict()
        self._key = None
        self._lr0_key = None

        if iterable:
            for item in iterable:
                self.add(item)

    def add(self, item):
        if hash(item) in self.map:
            return False
        self.map[hash(item)] = len(self.elements)
        self.elements.append(item)
        return True

    def pop(self):
        el = self.elements.pop()
        del self.map[hash(el)]
        return el

    def union(self, other, exclude=[]):
        excludes = OrderedSet(exclude)
        if not(type(other) in [list, set] or isinstance(other, OrderedSet)): return
        newset = deepcopy(self)
        for item in other:
            if item in exclude:
                continue
            newset.add(item)
        return newset

    def merge(self, other, exclude=[]):
        excludes = OrderedSet(exclude)
        if not(type(other) in [list, set] or isinstance(other, OrderedSet)): return
        for item in other:
            if item in exclude:
                continue
            self.add(item)
        return self

    def remove(self, item):
        h = hash(item)
        index = self.map.get(h)
        if index is None: return
        del self.elements[index]
        for i in range(index, len(self.elements)):
            self.map[hash(self.elements[i])] = i
        del self.map[h]

    def sort(self):
        newset = deepcopy(self)
        try:
            eltmp = list(zip(newset.map.keys(), map(lambda i: newset.elements[i], newset.map.values())))
            eltmp.sort(key=lambda e: e[1])
            newset.elements = list(map(lambda e: e[1], eltmp))
            newset.map = dict(zip(map(lambda e: hash(e), newset.elements), range(len(newset.elements))))
        except: pass
        return newset

    def __eq__(self, other):
        print("comparing", set(self.map.keys()), set(other.map.keys()))
        return set(self.map.keys()) == set(other.map.keys())

    def __contains__(self, item):
        return hash(item) in self.map

    def __len__(self):
        return len(self.elements)

    def __getitem__(self, key):
        if type(key) is int:
            return self.elements[key]
        elif type(key) is str:
            ind = self.map.get(key)
            if ind is None: return None
            return self.elements[ind]

    def __iter__(self):
        for item in self.elements:
            yield item

    def __repr__(self):
        return "[{}]".format(", ".join([repr(item) for item in self.elements]))