# Solution works for both single and doubly linked lists


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return "{} -> {}".format(self.val, self.next)


def reverse(head):
    if not head.next:
        new_head = Node(head.val)
        return new_head, new_head

    rev_head, rev_tail = reverse(head.next)
    rev_tail.next = Node(head.val)

    return rev_head, rev_tail.next


def is_palindrome(head):
    if not head:
        return None

    reversed_head = reverse(head)
    curr = head
    curr_rev = reversed_head[0]
    while curr:
        if curr.val != curr_rev.val:
            return False
        curr = curr.next
        curr_rev = curr_rev.next

    return True


# Tests

a0 = Node('a')
a1 = Node('a')
b0 = Node('b')
c0 = Node('c')

a0.next = b0
b0.next = c0

assert not is_palindrome(a0)
b0.next = a1
assert is_palindrome(a0)

a0 = Node('a')
assert is_palindrome(a0)
b0 = Node('b')
a0.next = b0
assert not is_palindrome(a0)
