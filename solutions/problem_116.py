from random import random, randint


class Node:
    def __init__(self, val):
        self.val = val
        self._left = None
        self._right = None

    def __repr__(self):
        string = "{"
        string += "{}: ".format(self.val)
        string += "{"
        string += "l: {}, ".format(self._left if self._left else -1)
        string += "r: {}".format(self._right if self._right else -1)
        string += "}"
        string += "}"

        return string

    @staticmethod
    def generate():
        return Node(randint(1, 100000))

    @property
    def left(self):
        if not self._left:
            self._left = Node.generate()
        return self._left

    @property
    def right(self):
        if not self._right:
            self._right = Node.generate()
        return self._right


tree_size = 100

a = Node.generate()
ref = a
nodes = set()
i = 0
while i < tree_size:
    ref = ref.left if random() < 0.5 else ref.right
    nodes.add(ref)

    i += 1

assert len(nodes) == tree_size
print(a)
