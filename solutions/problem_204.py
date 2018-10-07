class Node:
    def __init__(self):
        self.left = None
        self.right = None


def count_nodes(root):
    if not root:
        return 0

    count = 1
    count += count_nodes(root.left)
    count += count_nodes(root.right)

    return count


# Tests
a = Node()
b = Node()
c = Node()
d = Node()
e = Node()
a.left = b
a.right = c
b.left = d
b.right = e
assert count_nodes(a) == 5
f = Node()
c.left = f
assert count_nodes(a) == 6
