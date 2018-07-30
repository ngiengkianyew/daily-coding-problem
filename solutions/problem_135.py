import sys


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


def min_path_helper(root, path, path_sum):

    candidate_sum = path_sum + root.val
    candidate_path = path + [root.val]

    if not root.left and not root.right:
        return (candidate_sum, candidate_path)

    left_min_val, right_min_val = sys.maxsize, sys.maxsize
    if root.left:
        left_min_val, left_path = min_path_helper(
            root.left, candidate_path, candidate_sum)
    if root.right:
        right_min_val, right_path = min_path_helper(
            root.right, candidate_path, candidate_sum)

    return (left_min_val, left_path) if left_min_val < right_min_val \
        else (right_min_val, right_path)


def find_min_path(root):
    _, min_path = min_path_helper(root, list(), 0)
    return min_path


# Tests

a = Node(10)
b = Node(5)
c = Node(5)
a.left = b
a.right = c
d = Node(2)
b.right = d
e = Node(1)
c.right = e
f = Node(-1)
e.left = f
assert find_min_path(a) == [10, 5, 1, -1]

f.val = 5
assert find_min_path(a) == [10, 5, 2]
