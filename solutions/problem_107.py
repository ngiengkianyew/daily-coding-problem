class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def _print(self):
        print(self.val)
        if self.left:
            self.left._print()
        if self.right:
            self.right._print()


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

a._print()
