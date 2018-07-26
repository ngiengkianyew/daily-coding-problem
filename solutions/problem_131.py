class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.rand = None

    def __repr__(self):
        return self.val


def deep_clone(source):
    node_to_index = dict()
    node_index_to_rand_index = dict()

    curr = source
    i = 0
    while curr:
        node_to_index[curr] = i
        curr = curr.next
        i += 1

    curr = source
    i = 0
    while curr:
        rand_index = node_to_index[curr.rand]
        node_index_to_rand_index[i] = rand_index
        curr = curr.next
        i += 1

    dummy_head = Node('0')
    tail = dummy_head
    curr = source
    index_to_node = dict()
    i = 0
    while curr:
        new_node = Node(curr.val)
        index_to_node[i] = new_node
        curr = curr.next
        i += 1
        tail.next = new_node
        tail = new_node

    curr = dummy_head.next
    i = 0
    while curr:
        rand_index = node_index_to_rand_index[i]
        curr.rand = index_to_node[rand_index]
        curr = curr.next
        i += 1

    return dummy_head.next


# Tests

a = Node('a')
b = Node('b')
a.next = b
c = Node('c')
b.next = c
d = Node('d')
c.next = d
e = Node('e')
d.next = e

a.rand = a
b.rand = a
c.rand = e
d.rand = c
e.rand = c

cloned = deep_clone(a)
assert cloned.val == 'a'
assert cloned.rand.val == 'a'
assert cloned.next.val == 'b'
assert cloned.next.rand.val == 'a'
