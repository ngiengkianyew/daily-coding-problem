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


def swap_two_helper(node):
    if not node or not node.next:
        return node

    first = node
    second = node.next
    tail = swap_two_helper(second.next)

    second.next = first
    first.next = tail

    return second


def swap_two(head):
    dummy_head = Node(0)
    dummy_head.next = head

    return swap_two_helper(head)



# Tests
assert get_list(swap_two(get_nodes([1]))) == [1]
assert get_list(swap_two(get_nodes([1, 2]))) == [2, 1]
assert get_list(swap_two(get_nodes([1, 2, 3, 4]))) == [2, 1, 4, 3]
assert get_list(swap_two(get_nodes([1, 2, 3, 4, 5]))) == [2, 1, 4, 3, 5]
assert get_list(swap_two(get_nodes([1, 2, 3, 4, 5, 6]))) == [2, 1, 4, 3, 6, 5]
