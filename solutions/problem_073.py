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

def reverse_list(head, new_head):
    if not head:
        return new_head

    old_head = head.next
    head.next = new_head

    return reverse_list(old_head, head)


assert not get_list(reverse_list(get_nodes([]), None))
assert get_list(reverse_list(get_nodes([1]), None)) == [1]
assert get_list(reverse_list(get_nodes([1, 2]), None)) == [2, 1]
assert get_list(reverse_list(get_nodes([1, 2, 3]), None)) == [3, 2, 1]

