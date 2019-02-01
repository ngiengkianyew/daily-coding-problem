import random
from copy import deepcopy


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

    def __hash__(self):
        return hash(self.val)

    def __eq__(self, other):
        return self.val == other.val

    def __repr__(self):
        return str(self.val)


class LRUCache:
    def __init__(self, size):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = size
        self.recent_nodes = dict()

    def use(self, val):
        if val in self.recent_nodes:
            used_node = self.recent_nodes[val]
            used_node.prev = used_node.next
        elif len(self.recent_nodes) == self.size:
            used_node = Node(val)
            del self.recent_nodes[self.head.next.val]
            self.head.next = self.head.next.next
        else:
            used_node = Node(val)

        before_tail = self.tail.prev
        before_tail.next = used_node
        used_node.next = self.tail
        used_node.prev = before_tail
        self.tail.prev = used_node
        self.recent_nodes[val] = used_node


def count_playlists(song_ids, cache, plays_left):
    if plays_left == 0:
        return 1

    total = 0
    for song_id in song_ids:
        if song_id in cache.recent_nodes:
            continue
        new_cache = deepcopy(cache)
        new_cache.use(song_id)
        total += count_playlists(song_ids, new_cache, plays_left - 1)

    return total


def get_valid_playlists(plays, songs, buffer):
    song_ids = set(range(songs))
    lru_cache = LRUCache(buffer)

    total = count_playlists(song_ids, lru_cache, plays)
    return total


# Tests
assert get_valid_playlists(6, 4, 2) > get_valid_playlists(6, 4, 3)
