class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRU:
    def __init__(self, cache_limit):
        self.cache_limit = cache_limit
        self.cache_contents = dict()
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node):
        prev_node = self.tail.prev
        node.next = self.tail
        node.prev = prev_node
        prev_node.next = node
        self.tail.prev = node

    def set_value(self, key, value):
        if key in self.cache_contents:
            node = self.cache_contents[key]
            self._remove(node)
        node = Node(key, value)
        self._add(node)
        self.cache_contents[key] = node
        if len(self.cache_contents) > self.cache_limit:
            node_to_delete = self.head.next
            self._remove(node_to_delete)
            del self.cache_contents[node_to_delete.key]

    def get_value(self, key):
        if key in self.cache_contents:
            node = self.cache_contents[key]
            self._remove(node)
            self._add(node)
            return node.value

        return None


lru = LRU(cache_limit=3)

assert not lru.get_value("a")
lru.set_value("a", 1)
assert lru.get_value("a") == 1
lru.set_value("b", 2)
lru.set_value("c", 3)
lru.set_value("d", 4)
lru.set_value("e", 5)
lru.set_value("a", 1)
assert lru.get_value("a") == 1
assert not lru.get_value("b")
assert lru.get_value("e") == 5
assert not lru.get_value("c")
