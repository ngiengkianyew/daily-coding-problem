class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        string = "["
        node = self
        while node:
            string += "{} ->".format(node.val)
            node = node.next
        string += "None]"
        return string


def get_nodes(values):
    next_node = None
    for value in values[::-1]:
        node = Node(value)
        node.next = next_node
        next_node = node

    return next_node


def get_list(head):
    node = head
    nodes = list()
    while node:
        nodes.append(node.val)
        node = node.next
    return nodes


def rotate_ll(llist, k):
    cnode = llist
    head = cnode
    size = 0
    while cnode:
        tail = cnode
        cnode = cnode.next
        size += 1

    new_head = llist
    new_tail = None
    for _ in range(size - k):
        new_tail = new_head
        new_head = new_head.next

    tail.next = head
    new_tail.next = None

    return new_head


# Tests

assert get_list(rotate_ll(get_nodes([7, 7, 3, 5]), 2)) == [3, 5, 7, 7]
assert get_list(rotate_ll(get_nodes([1, 2, 3, 4, 5]), 3)) == [3, 4, 5, 1, 2]
