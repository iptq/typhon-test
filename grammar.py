# pylint: disable=W0614
from constants import *

class Grammar(object):
    def __init__(self, classes, mode):
        self.classes = classes
        self.productions = []
        self.augmented = None
