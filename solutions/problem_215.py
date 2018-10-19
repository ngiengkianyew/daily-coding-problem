class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.depth = None

    def __repr__(self):
        return "Node[val={}]".format(self.data)


def compute_bottom_view(root, depths, depth, width):
    root.depth = depth

    if width not in depths or depths[width].depth < depth:
        depths[width] = root

    if root.right:
        compute_bottom_view(root.right, depths, depth + 1, width + 1)
    if root.left:
        compute_bottom_view(root.left, depths, depth + 1, width - 1)


def get_bottom_view(root):
    depths = dict()
    compute_bottom_view(root, depths, 0, 0)

    sorted_items = sorted(depths.items(), key=lambda x: x[0])
    return [x[1].data for x in sorted_items]


# Tests
root = Node(5)
root.left = Node(3)
root.left.left = Node(1)
root.left.left.left = Node(0)
root.left.right = Node(4)
root.right = Node(7)
root.right.left = Node(6)
root.right.right = Node(9)
root.right.right.left = Node(8)
assert get_bottom_view(root) == [0, 1, 3, 6, 8, 9]
