from typing import List


class Node:
    def __init__(self, val: int):
        self.val = val
        self.l = None
        self.r = None

    def __repr__(self):
        return "{}=[l->{}, r->{}]".format(self.val, self.l, self.r)


def make_cartree(arr: List[int], last: Node, root: Node):
    if not arr:
        return root

    node = Node(arr[0])
    if not last:
        return make_cartree(arr[1:], node, node)

    if last.val > node.val:
        node.l = last
        return make_cartree(arr[1:], node, node)

    last.r = node
    return make_cartree(arr[1:], last, last)


# Tests
cartree = make_cartree([3, 2, 6, 1, 9], None, None)
assert str(cartree) == \
    "1=[l->2=[l->3=[l->None, r->None], " + \
    "r->6=[l->None, r->None]], " + \
    "r->9=[l->None, r->None]]"
