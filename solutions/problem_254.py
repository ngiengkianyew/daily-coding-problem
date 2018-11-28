class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return "{}=[{},{}]".format(self.val, self.left, self.right)

    def __hash__(self):
        return hash(self.val)


def recover_full(root):
    if not root.left and not root.right:
        return root
    elif root.left and root.right:
        root.left = recover_full(root.left)
        root.right = recover_full(root.right)
        return root
    elif root.left:
        return recover_full(root.left)
    elif root.right:
        return recover_full(root.right)


# Tests
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")

a.left = b
a.right = c
b.left = d
d.right = f
c.right = e
e.left = g
e.right = h

print(a)
print(recover_full(a))
