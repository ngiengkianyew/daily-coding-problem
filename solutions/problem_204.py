class Node:
    def __init__(self):
        self.left = None
        self.right = None


def count_nodes(root, lspine=0, rspine=0):
    if not root:
        return 0

    if not lspine:
        node = root
        while node:
            node = node.left
            lspine += 1
    if not rspine:
        node = root
        while node:
            node = node.right
            rspine += 1

    if lspine == rspine:
        return 2**lspine - 1

    return 1 + \
        count_nodes(root.left, lspine=lspine-1) + \
        count_nodes(root.right, rspine=rspine-1)


# Tests
a = Node()
b = Node()
c = Node()
a.left = b
a.right = c
assert count_nodes(a) == 3
d = Node()
b.left = d
assert count_nodes(a) == 4
e = Node()
b.right = e
assert count_nodes(a) == 5
f = Node()
c.left = f
assert count_nodes(a) == 6
