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


def get_intersection_node(list_a, list_b):

    def get_list_length(linked_list):
        length = 0
        node = linked_list
        while node:
            length += 1
            node = node.next

        return length

    len_a, len_b = get_list_length(list_a), get_list_length(list_b)
    min_len = min(len_a, len_b)

    for _ in range(len_a - min_len):
        list_a = list_a.next
    for _ in range(len_b - min_len):
        list_b = list_b.next

    node_a = list_a
    node_b = list_b
    for _ in range(min_len):
        if node_a.val == node_b.val:
            return node_a
        node_a = node_a.next
        node_b = node_b.next

    return None


assert not get_intersection_node(
    get_nodes([]), get_nodes([]))
assert get_intersection_node(
    get_nodes([0, 3, 7, 8, 10]), get_nodes([99, 1, 8, 10])).val == 8
assert get_intersection_node(
    get_nodes([7, 8, 10]), get_nodes([99, 1, 8, 10])).val == 8
