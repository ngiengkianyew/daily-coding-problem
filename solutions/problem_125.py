class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


def get_array(root):
    arr = [root]

    if not root.left and not root.right:
        return arr

    if root.left:
        arr = get_array(root.left) + arr
    if root.right:
        arr = arr + get_array(root.right)

    return arr


def search_pair(root, val):
    arr = get_array(root)
    i, k = 0, len(arr) - 1
    while i < k:
        summed = arr[i].val + arr[k].val
        if summed == val:
            return (arr[i], arr[k])
        elif summed < val:
            i += 1
        else:
            k -= 1


# Tests
a = Node(10)
b = Node(5)
c = Node(15)
d = Node(11)
e = Node(15)
a.left = b
a.right = c
c.left = d
c.right = e

assert search_pair(a, 15) == (b, a)
assert search_pair(a, 20) == (b, e)
assert search_pair(a, 30) == (c, e)
assert search_pair(a, 26) == (d, e)
