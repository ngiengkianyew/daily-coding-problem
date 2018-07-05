class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


def get_all_paths(node):
    if not node:
        return []

    node_paths = list()
    left_paths = get_all_paths(node.left)
    for path in left_paths:
        node_paths.append([node.val] + path)

    right_paths = get_all_paths(node.right)
    for path in right_paths:
        node_paths.append([node.val] + path)

    return node_paths if node_paths else [[node.val]]


# Tests

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.left = b
a.right = c
c.left = d
c.right = e

assert get_all_paths(a) == [[1, 2], [1, 3, 4], [1, 3, 5]]
assert get_all_paths(b) == [[2]]
assert get_all_paths(c) == [[3, 4], [3, 5]]
