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


def partition(llist, k):
    head = llist
    prev, curr = head, head.next

    while curr:
        if curr.val < k:
            prev.next = curr.next
            curr.next = head
            head = curr
            curr = prev.next
        else:
            prev = curr
            curr = curr.next

    return head


# Tests
assert get_list(partition(get_nodes([5, 1, 8, 0, 3]), 3)) == [0, 1, 5, 8, 3]
