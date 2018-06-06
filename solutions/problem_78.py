import sys
from heapq import heappush, heappop


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


def merge_lists(all_lists):
    merged_head = Node(None)
    merged_tail = merged_head
    candidates = list()
    counter = 0
    for llist in all_lists:
        heappush(candidates, (llist.val, counter, llist))
        counter += 1

    while candidates:
        _, _, new_node = heappop(candidates)

        if new_node.next:
            heappush(candidates, (new_node.next.val, counter, new_node.next))
            counter += 1

        merged_tail.next = new_node
        merged_tail = new_node

    return merged_head.next


assert get_list(merge_lists([get_nodes([1, 4, 6]),
                             get_nodes([1, 3, 7])])) == [1, 1, 3, 4, 6, 7]
assert get_list(merge_lists([get_nodes([1, 4, 6]),
                             get_nodes([2, 3, 9]),
                             get_nodes([1, 3, 7])])) == [1, 1, 2, 3, 3, 4, 6, 7, 9]

