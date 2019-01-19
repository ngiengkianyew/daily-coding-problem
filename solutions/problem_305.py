class Node:
    def __init__(self, x):
        self.val = x
        self.cum = 0
        self.next = None

    def __str__(self):
        string = "["
        node = self
        while node:
            string += "{},{} ->".format(node.val, node.cum)
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


def add_cum_sum(head):
    node = head
    cum_sum = 0
    while node:
        node.cum = node.val + cum_sum
        cum_sum = node.cum
        node = node.next


def remove_zero_sum(head):
    add_cum_sum(head)
    dummy_head = Node(None)
    dummy_head.next = head

    seen_totals = dict()
    node = dummy_head
    index = 0
    while node:
        if node.cum in seen_totals:
            seen_totals[node.cum].next = node.next
        seen_totals[node.cum] = node
        index += 1
        node = node.next

    return dummy_head.next


# Tests
llist = get_nodes([3, 4, -7, 5, -6, 6])
assert get_list(remove_zero_sum(llist)) == [5]
