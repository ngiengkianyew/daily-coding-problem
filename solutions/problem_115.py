class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

    def is_exact_tree(self, other):
        if self.val != other.val:
            return False
        if bool(self.left) ^ bool(other.left):
            return False
        if bool(self.right) ^ bool(other.right):
            return False

        check = True
        if self.left:
            check = check and self.left.is_exact_tree(other.left)
        if self.right:
            check = check and self.right.is_exact_tree(other.right)

        return check

    def is_subtree(self, other):
        if self.is_exact_tree(other):
            return True

        if self.left and self.left.is_subtree(other):
            return True

        if self.right and self.right.is_subtree(other):
            return True

        return False


# Tests

s_0 = Node(0)
s_1 = Node(1)
s_2 = Node(2)
s_0.left = s_1
s_0.right = s_2
s_3 = Node(3)
s_4 = Node(4)
s_2.left = s_3
s_2.right = s_4

t_0 = Node(2)
t_1 = Node(3)
t_2 = Node(4)
t_0.left = t_1
t_0.right = t_2

r_0 = Node(2)
r_1 = Node(3)
r_2 = Node(5)
r_0.left = r_1
r_0.right = r_2

assert s_2.is_exact_tree(t_0)
assert s_0.is_subtree(t_0)
assert not s_0.is_subtree(r_0)
