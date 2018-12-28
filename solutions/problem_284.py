class Node:
    def __init__(self, val):
        self.val = val
        self.lev = None
        self.l = None
        self.r = None
        self.p = None

    def __repr__(self):
        return "{} = (l={}, r={})".format(self.val, self.l, self.r)

    def __hash__(self):
        return hash(self.val)


def populate_level_map(node, level_map, parent=None, level=0):
    if not node:
        return

    node.p = parent
    node.lev = level

    if level not in level_map:
        level_map[level] = set()
    level_map[level].add(node)

    populate_level_map(node.l, level_map, node, level + 1)
    populate_level_map(node.r, level_map, node, level + 1)


def get_cousins(root, node):
    level_map = dict()
    populate_level_map(root, level_map)

    cousins = set([x for x in level_map[node.lev] if x.p != node.p])
    return cousins


# Tests
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
a.l, a.r = b, c
b.l, b.r = d, e
c.r = f

assert get_cousins(a, d) == {f}
assert get_cousins(a, f) == {d, e}
assert get_cousins(a, a) == set()
assert get_cousins(a, c) == set()
