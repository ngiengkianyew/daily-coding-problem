# The problem description is needlessly complicated.
# The problem is the same as finding the intersection of linked list


class Node:
    def __init__(self):
        self.parent = None


def get_list_length(node):
    if not node:
        return 0

    return 1 + get_list_length(node.parent)


def get_lca(node_a, node_b):
    len_a = get_list_length(node_a)
    len_b = get_list_length(node_b)

    (longer, max_len, shorter, min_len) = \
        (node_a, len_a, node_b, len_b) if len_a > len_b \
        else (node_b, len_b, node_a, len_a)

    for _ in range(max_len - min_len):
        longer = longer.parent

    while longer and shorter:
        if longer == shorter:
            return longer

        longer = longer.parent
        shorter = shorter.parent


# Test
def test_1():
    a = Node()
    b = Node()
    c = Node()
    d = Node()
    e = Node()
    f = Node()
    g = Node()

    a.parent = c
    c.parent = e
    e.parent = f

    b.parent = d
    d.parent = f

    f.parent = g

    assert get_lca(a, b) == f


def test_2():
    a = Node()
    b = Node()
    c = Node()
    d = Node()
    e = Node()
    f = Node()
    g = Node()

    a.parent = c
    c.parent = e

    b.parent = d
    d.parent = e

    e.parent = f
    f.parent = g

    assert get_lca(a, b) == e
    assert get_lca(c, b) == e
    assert get_lca(e, b) == e


test_1()
test_2()
