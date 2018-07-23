class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def solve_graph(root):
    if root.val.isnumeric():
        return float(root.val)

    return eval("{} {} {}".format(solve_graph(root.left), root.val, solve_graph(root.right)))


d = Node("3")
e = Node("2")
f = Node("4")
g = Node("5")

b = Node("+")
b.left = d
b.right = e

c = Node("+")
c.left = f
c.right = g

a = Node("*")
a.left = b
a.right = c


assert solve_graph(a) == 45
assert solve_graph(c) == 9
assert solve_graph(b) == 5
assert solve_graph(d) == 3
