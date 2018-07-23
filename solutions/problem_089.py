import sys


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_valid_bst_node_helper(node, lb, ub):

    if node and node.val <= ub and node.val >= lb:
        return is_valid_bst_node_helper(node.left, lb, node.val) and \
            is_valid_bst_node_helper(node.right, node.val, ub)

    return not node  # if node is None, it's a valid BST


def is_valid_bst(root):
    return is_valid_bst_node_helper(root, -sys.maxsize, sys.maxsize)


# Tests


assert is_valid_bst(None)

a = Node(3)
b = Node(2)
c = Node(6)
d = Node(1)
e = Node(3)
f = Node(4)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
assert is_valid_bst(a)


a = Node(1)
b = Node(2)
c = Node(6)
d = Node(1)
e = Node(3)
f = Node(4)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
assert not is_valid_bst(a)

a = Node(3)
b = Node(2)
c = Node(6)
d = Node(1)
e = Node(4)
f = Node(4)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
assert not is_valid_bst(a)
