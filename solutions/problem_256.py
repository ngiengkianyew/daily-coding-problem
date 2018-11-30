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


def rearrange(llist):
    if not llist.next:
        return llist

    arr = get_list(llist)
    arr.sort()

    for i in range(2, len(arr), 2):
        tmp = arr[i]
        arr[i] = arr[i-1]
        arr[i-1] = tmp

    return get_nodes(arr)


# Tests
assert get_list(rearrange(get_nodes([1, 2, 3, 4, 5]))) == [1, 3, 2, 5, 4]
