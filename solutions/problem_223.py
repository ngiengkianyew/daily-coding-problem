class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return "{}=[l={}, r={}]".format(self.val, self.left, self.right)


def add_reverse_links(root, parent=None):
    root.parent = parent

    if root.left:
        add_reverse_links(root.left, root)
    if root.right:
        add_reverse_links(root.right, root)


def print_inorder(root):
    if root.left:
        print_inorder(root.left)

    print(root.val)

    if root.right:
        print_inorder(root.right)


# Tests
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
d.right = h
# print(a)

add_reverse_links(a)
assert h.parent == d
assert g.parent == c

print_inorder(a)
