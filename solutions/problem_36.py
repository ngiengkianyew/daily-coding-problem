class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


def find_largest_and_parent(node):
    parent = None
    while node.right:
        parent = node
        node = node.right

    return node, parent


def find_second_largest(root):
    if not root:
        return None

    second_largest = None
    if root.left and not root.right:
        second_largest, _ = find_largest_and_parent(root.left)
    else:
        _, second_largest = find_largest_and_parent(root)
    print("second_largest", second_largest)

    return second_largest


def test_0():
    node_a = Node(5)

    assert not find_second_largest(node_a)


def test_1():
    node_a = Node(5)
    node_b = Node(3)
    node_c = Node(8)
    node_d = Node(2)
    node_e = Node(4)
    node_f = Node(7)
    node_g = Node(9)
    node_a.left = node_b
    node_a.right = node_c
    node_b.left = node_d
    node_b.right = node_e
    node_c.left = node_f
    node_c.right = node_g

    assert find_second_largest(node_a).data == 8


def test_2():
    node_a = Node(5)
    node_b = Node(3)
    node_d = Node(2)
    node_e = Node(4)
    node_a.left = node_b
    node_b.left = node_d
    node_b.right = node_e

    assert find_second_largest(node_a).data == 4


test_0()
test_1()
test_2()
