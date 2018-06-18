import sys


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        string = "val={}:(left={}, right={})".format(
            self.val, self.left, self.right)
        return string


def get_largest_bst_helper(node):
    if not node:
        return (True, node, 0, sys.maxsize, -sys.maxsize)
    if not node.left and not node.right:
        return (True, node, 1, node.val, node.val)

    left_is_bst, left_bst, left_nodes, left_minval, left_maxval = \
        get_largest_bst_helper(node.left)
    right_is_bst, right_bst, right_nodes, right_minval, right_maxval = \
        get_largest_bst_helper(node.right)

    if left_is_bst and right_is_bst:
        if node.left and node.right:
            if node.val >= left_maxval and node.val <= right_minval:
                return (True, node, left_nodes + right_nodes + 1,
                        left_minval, right_maxval)
        elif node.left and node.val >= left_maxval:
            return (True, node, left_nodes + 1, left_minval, node.val)
        elif node.right and node.val >= right_minval:
            return (True, node, left_nodes + 1, node.val, right_maxval)

    if left_nodes > right_nodes:
        return (False, left_bst, left_nodes, left_minval, node.val)
    else:
        return (False, right_bst, right_nodes, node.val, right_maxval)


def get_largest_bst(root):
    _, largest_bst, nodes, _, _ = get_largest_bst_helper(root)
    return (largest_bst, nodes)


# tests

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
assert get_largest_bst(a) == (a, 6)

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
assert get_largest_bst(a) == (b, 3)

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
assert get_largest_bst(a) == (b, 3)

a = Node(3)
b = Node(2)
c = Node(6)
d = Node(1)
e = Node(1)
f = Node(4)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
assert get_largest_bst(a) == (c, 2)
