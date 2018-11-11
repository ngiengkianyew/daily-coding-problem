class Node:
    def __init__(self, val):
        self.val = val
        self.children = list()

    def __repr__(self):
        return "{} -> {}".format(self.val, self.children)


def update_levels_dict(root, levels, lnum):
    if lnum not in levels:
        levels[lnum] = list()

    levels[lnum].append(root.val)
    for child in root.children:
        update_levels_dict(child, levels, lnum + 1)


def is_symmetric(tree):
    levels = dict()
    update_levels_dict(tree, levels, 0)

    for level in levels:
        arr = levels[level]
        if arr != arr[::-1]:
            return False

    return True


# Tests
e = Node(9)
f = Node(9)
d = Node(3)
d.children = [e]
c = Node(3)
c.children = [f]
b = Node(5)
a = Node(4)
a.children = [c, b, d]
assert is_symmetric(a)

c.val = 4
assert not is_symmetric(a)
