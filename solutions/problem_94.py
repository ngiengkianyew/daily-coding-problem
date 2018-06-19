class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def get_max_path_sum(root, current_max_sum, overall_max_sum):
    if not root:
        return overall_max_sum

    current_max_sum = max(root.val, current_max_sum + root.val)
    overall_max_sum = max(overall_max_sum, current_max_sum)

    left_path_sum = get_max_path_sum(
        root.left, current_max_sum, overall_max_sum)
    right_path_sum = get_max_path_sum(
        root.right, current_max_sum, overall_max_sum)

    return max(overall_max_sum, left_path_sum, right_path_sum)


assert get_max_path_sum(None, 0, 0) == 0

a = Node(1)
assert get_max_path_sum(a, 0, 0) == 1

b = Node(2)
a.left = b
assert get_max_path_sum(a, 0, 0) == 3

c = Node(3)
a.right = c
assert get_max_path_sum(a, 0, 0) == 4

a.val = -1
assert get_max_path_sum(a, 0, 0) == 3

d = Node(4)
b.left = d
assert get_max_path_sum(a, 0, 0) == 6
