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


def remove_kth_last(head, k):
    if not head or not k:
        return head

    dummy = Node(None)
    dummy.next = head
    runner = head

    for _ in range(k):
        runner = runner.next

    current_node = dummy
    while runner:
        runner = runner.next
        current_node = current_node.next

    current_node.next = current_node.next.next

    return dummy.next


assert get_list(remove_kth_last(
    get_nodes([]), 1)) == []
assert get_list(remove_kth_last(
    get_nodes([0, 3, 7, 8, 10]), 2)) == [0, 3, 7, 10]
assert get_list(remove_kth_last(
    get_nodes([7, 8, 10]), 3)) == [8, 10]
assert get_list(remove_kth_last(
    get_nodes([7, 8, 10]), 1)) == [7, 8]
