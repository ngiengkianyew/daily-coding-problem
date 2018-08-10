class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        string = "{}=[l={}, r={}]".format(self.val, self.left, self.right)
        return string

    def prune(self):
        if not self.left and not self.right and not self.val:
            return None

        if self.left:
            self.left = self.left.prune()
        if self.right:
            self.right = self.right.prune()

        return self


# Tests
root = Node(0)
root.left = Node(1)
root.right = Node(0)
root.right.left = Node(1)
root.right.right = Node(0)
root.right.left.left = Node(0)
root.right.left.right = Node(0)

assert root.right.right
assert root.right.left.left
assert root.right.left.right
root.prune()

assert not root.right.right
assert not root.right.left.left
assert not root.right.left.right

assert root.left
assert root.right
