class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def get_freq_tree_sum(root, counts):
    if not root:
        return 0

    tree_sum = root.val + \
        get_freq_tree_sum(root.left, counts) + \
        get_freq_tree_sum(root.right, counts)

    if not tree_sum in counts:
        counts[tree_sum] = 0
    counts[tree_sum] += 1

    return tree_sum


def get_freq_tree_sum_helper(root):
    counts = dict()
    get_freq_tree_sum(root, counts)

    return max(counts.items(), key=lambda x: x[1])[0]


# Tests
root = Node(5)
root.left = Node(2)
root.right = Node(-5)
assert get_freq_tree_sum_helper(root) == 2
