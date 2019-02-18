class Node:
    def __init__(self, val):
        self.val = val
        self.l, self.r = None, None


def get_distinct_ways(node):
    if node and node.l and node.r:
        return 2 * get_distinct_ways(node.l) * get_distinct_ways(node.r)

    return 1


# Tests
a = Node(3)
b = Node(2)
c = Node(1)
a.l = b
a.r = c
assert get_distinct_ways(a) == 2
