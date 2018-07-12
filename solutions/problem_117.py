import sys


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return "{}=(l={}, r={})".format(self.val, self.left, self.right)


def get_maxsum_level_helper(level, nodes, parent_sum):
    child_nodes = list()
    nodes_sum = 0
    for node in nodes:
        nodes_sum += node.val
        if node.left:
            child_nodes.append(node.left)
        if node.right:
            child_nodes.append(node.right)

    max_sum = max(nodes_sum, parent_sum)
    if child_nodes:
        max_sum = get_maxsum_level_helper(level + 1, child_nodes, max_sum)

    return max_sum


def get_maxsum_level(root):
    max_sum = get_maxsum_level_helper(0, [root], -sys.maxsize)
    return max_sum


a = Node(1)
b = Node(2)
c = Node(3)
a.left = b
a.right = c

d = Node(4)
e = Node(5)
b.left = d
b.right = e

f = Node(6)
g = Node(7)
c.left = f
c.right = g

h = Node(8)
d.right = h

assert get_maxsum_level(a) == 22
a.val = 100
assert get_maxsum_level(a) == 100
b.val = 150
assert get_maxsum_level(a) == 153
h.val = 200
assert get_maxsum_level(a) == 200
