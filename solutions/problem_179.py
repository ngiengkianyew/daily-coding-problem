class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return "{} => (l: {}, r: {})".format(
            self.data, self.left, self.right)


def get_tree(seq):
    head = Node(seq[-1])
    if len(seq) == 1:
        return head

    for i in range(len(seq) - 1):
        if seq[i] > head.data:
            sep_ind = i
            break

    leq, gt = seq[:sep_ind], seq[sep_ind:-1]

    head.left = get_tree(leq) if leq else None
    head.right = get_tree(gt) if gt else None

    return head


# Tests
tree = get_tree([2, 4, 3, 8, 7, 5])
assert tree.data == 5
assert tree.left.data == 3
assert tree.right.data == 7
assert tree.left.left.data == 2
assert tree.left.right.data == 4
assert tree.right.right.data == 8
