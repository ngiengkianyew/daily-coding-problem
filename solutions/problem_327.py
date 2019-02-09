class Node:
    def __init__(self, val):
        self.val = val
        self.l = None
        self.r = None

    def __repr__(self):
        return "{}".format(self.val)


def merge(t1, t2, final_prev, left):
    if not t1 and not t2:
        return

    if t1 and t2:
        final_node = Node(t1.val + t2.val)
        if left:
            final_prev.l = final_node
        else:
            final_prev.r = final_node
        merge(t1.l, t2.l, final_node, True)
        merge(t1.r, t2.r, final_node, False)
        return

    only_node = t1 if t1 else t2
    if left:
        final_prev.l = only_node
    else:
        final_prev.r = only_node


# Tests
root_1 = Node(1)
root_1.l = Node(2)
root_1.r = Node(3)
root_1.l.l = Node(4)

root_2 = Node(2)

final_root = Node(0)
merge(root_1, root_2, final_root, True)
assert final_root.l.val == 3
