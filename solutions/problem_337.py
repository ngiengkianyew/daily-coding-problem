from random import shuffle


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


def unishuffle(llist):
    length = 0
    node = ll
    node_list = list()
    while node:
        node_list.append(node)
        node = node.next
        length += 1

    shuffle(node_list)

    dummy = Node(None)
    for node in node_list:
        node.next = dummy.next
        dummy.next = node

    return dummy.next


# Tests
ll = get_nodes([1, 2, 3, 4, 5])
print(unishuffle(ll))
