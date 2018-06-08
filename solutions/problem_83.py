class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        string = "{}=({},{})".format(self.val, self.left, self.right)
        return string


def invert_tree(root):
    if not root:
        return

    inverted_left = invert_tree(root.right)
    inverted_right = invert_tree(root.left)
    root.left = inverted_left
    root.right = inverted_right

    return root


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f

inverted_a = invert_tree(a)
assert inverted_a.left == c
assert inverted_a.right == b
assert inverted_a.left.right == f
assert inverted_a.right.right == d
