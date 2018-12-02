class Node:
    def __init__(self, val):
        self.val = val
        self.ln = None
        self.rn = None

    def __repr__(self):
        return "Node=({}, ln={}, rn={})".format(
            self.val, self.ln, self.rn)


def get_bfs_alt(root, level, level_dict):
    if not root:
        return

    if level not in level_dict:
        level_dict[level] = list()
    level_dict[level].append(root.val)

    get_bfs_alt(root.ln, level + 1, level_dict)
    get_bfs_alt(root.rn, level + 1, level_dict)


def get_boustrophedon(root):
    level_dict = dict()
    get_bfs_alt(root, 0, level_dict)

    final_order = list()
    for i in range(len(level_dict)):
        final_order.extend(reversed(level_dict[i]) if i % 2 else level_dict[i])

    return final_order


# Tests
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)

n2.ln = n4
n2.rn = n5
n3.ln = n6
n3.rn = n7
n1.ln = n2
n1.rn = n3

assert get_boustrophedon(n1) == [1, 3, 2, 4, 5, 6, 7]
