class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


def find_deepest_node(root, depth):
    if not root.left and not root.right:
        return (root, depth)

    left_depth = depth
    right_depth = depth
    if root.left:
        left_deepest, left_depth = find_deepest_node(root.left, depth + 1)
    if root.right:
        right_deepest, right_depth = find_deepest_node(root.right, depth + 1)

    return (left_deepest, left_depth) if left_depth > right_depth \
        else (right_deepest, right_depth)


def find_deepest_node_helper(root):
    return find_deepest_node(root, 0)[0]


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d

assert find_deepest_node_helper(a) == d

c.left = e
e.left = f


assert find_deepest_node_helper(a) == f
