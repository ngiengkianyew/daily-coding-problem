from typing import List, Dict
from copy import deepcopy


class AppleSet:
    def __init__(self):
        self.apple_types = dict()

    def __repr__(self):
        return str(self.apple_types)

    def add_apple(self, atype: int):
        if atype not in self.apple_types:
            self.apple_types[atype] = 0
        self.apple_types[atype] += 1

    def remove_apple(self, atype: int):
        self.apple_types[atype] -= 1
        if self.apple_types[atype] == 0:
            del self.apple_types[atype]

    def size(self):
        return len(self.apple_types)

    def total(self):
        return sum(x for x in self.apple_types.values())


def get_min_set(apple_set: AppleSet, apples: List[int]):
    if apple_set.size() == 2:
        return apple_set.total()
    if not apples:
        return 0

    first, last = apples[0], apples[-1]

    apple_set_1 = deepcopy(apple_set)
    apple_set_1.remove_apple(first)
    alt_1 = get_min_set(apple_set_1, apples[1:])

    apple_set_2 = deepcopy(apple_set)
    apple_set_2.remove_apple(last)
    alt_2 = get_min_set(apple_set_2, apples[:-1])

    return max(alt_1, alt_2)


def get_longest_portion(apples: List[int]):
    apple_set = AppleSet()
    for atype in apples:
        apple_set.add_apple(atype)

    return get_min_set(apple_set, apples)


# Tests
assert get_longest_portion([2, 1, 2, 3, 3, 1, 3, 5]) == 4
assert get_longest_portion([2, 1, 2, 2, 2, 1, 2, 1]) == 8
assert get_longest_portion([1, 2, 3, 4]) == 2
