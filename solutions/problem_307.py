import bisect


class Node:
    def __init__(self, val):
        self.val = val
        self.l = None
        self.r = None


def get_arr(root):
    if not root:
        return list()

    return get_arr(root.l) + [root.val] + get_arr(root.r)


def get_fc(root, val):
    arr = get_arr(root)
    ind = bisect.bisect(arr, val)
    if ind == 0:
        return None, arr[0]
    elif ind == len(arr):
        return arr[-1], None
    elif val == arr[ind-1]:
        return val, val
    else:
        return arr[ind-1], arr[ind]


# Tests
a = Node(4)
b = Node(2)
c = Node(1)
d = Node(3)
b.l = c
b.r = d
e = Node(6)
a.l = b
a.r = e

assert get_fc(a, 2) == (2, 2)
assert get_fc(a, 7) == (6, None)
assert get_fc(a, -1) == (None, 1)
assert get_fc(a, 5) == (4, 6)
