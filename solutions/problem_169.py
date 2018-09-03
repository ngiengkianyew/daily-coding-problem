import sys


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


def merge_sorted_lists(list_a, list_b):
    head = Node(-sys.maxsize)
    node = head
    node_a = list_a
    node_b = list_b

    while node_a and node_b:
        if node_a.val < node_b.val:
            tmp = node_a
            node_a = node_a.next
        else:
            tmp = node_b
            node_b = node_b.next
        tmp.next = None
        node.next = tmp
        node = node.next

    if node_a:
        node.next = node_a
    if node_b:
        node.next = node_b

    return head.next


def sort_ll_helper(llist, node_count):
    if node_count == 1:
        return llist

    mid = node_count // 2
    right_head = llist
    left_tail = None
    for _ in range(mid):
        left_tail = right_head
        right_head = right_head.next

    left_tail.next = None

    sorted_left = sort_ll_helper(llist, mid)
    sorted_right = sort_ll_helper(right_head, node_count - mid)

    return merge_sorted_lists(sorted_left, sorted_right)


def sort_ll(llist):
    count = 0
    node = llist
    while node:
        count += 1
        node = node.next

    return sort_ll_helper(llist, count)


# Tests
llist = get_nodes([4, 1, -3, 99])
assert get_list(sort_ll(llist)) == [-3, 1, 4, 99]
