class Node:
    def __init__(self):
        self.left = None
        self.right = None


def get_height(root):
    if not root:
        return 0

    left_height = get_height(root.left)
    right_height = get_height(root.right)

    return max(left_height, right_height) + 1


def is_balanced(root):
    left_height = get_height(root.left)
    right_height = get_height(root.right)

    return True if abs(left_height - right_height) < 2 else False


# Tests
a = Node()
b = Node()
c = Node()
a.left = b
assert is_balanced(a)
a.right = c
assert is_balanced(a)
d = Node()
e = Node()
b.left = d
d.left = e
assert not is_balanced(a)
