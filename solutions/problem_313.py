from typing import Set


class Combo:
    def __init__(self, key_1: int, key_2: int, key_3: int):
        self.key_1 = key_1 if key_1 > -1 else key_1 + 10
        self.key_2 = key_2 if key_1 > -1 else key_1 + 10
        self.key_3 = key_3 if key_1 > -1 else key_1 + 10

    def __hash__(self):
        return hash((self.key_1, self.key_2, self.key_3))

    def __eq__(self, other):
        return \
            self.key_1 == other.key_1 and \
            self.key_2 == other.key_2 and \
            self.key_3 == other.key_3

    def __repr__(self):
        return "{}-{}-{}".format(self.key_1, self.key_2, self.key_3)


def get_moves(target: Combo, deadends: Set[Combo],
              start: Combo = Combo(0, 0, 0)):
    if start == target:
        return 0
    elif start in deadends:
        return None

    if start.key_1 != target.key_1:
        k1_moves = list()
        k1_diff = abs(start.key_1 - target.key_1)
        k1_new_start = Combo(target.key_1, start.key_2, start.key_3)
        k1_moves = [
            k1_diff + get_moves(target, deadends, k1_new_start),
            (10 - k1_diff) + get_moves(target, deadends, k1_new_start)
        ]
        k1_moves = [x for x in k1_moves if x]
        if k1_moves:
            return min(k1_moves)

    if start.key_2 != target.key_2:
        k2_moves = list()
        k2_diff = abs(start.key_1 - target.key_1)
        k2_new_start = Combo(start.key_1, target.key_2, start.key_3)
        k2_moves = [
            k2_diff + get_moves(target, deadends, k2_new_start),
            (10 - k2_diff) + get_moves(target, deadends, k2_new_start)
        ]
        k2_moves = [x for x in k2_moves if x]
        if k2_moves:
            return min(k2_moves)

    if start.key_2 != target.key_3:
        k3_moves = list()
        k3_diff = abs(start.key_1 - target.key_1)
        k3_new_start = Combo(start.key_1, start.key_2, target.key_3)
        k3_moves = [
            k3_diff + get_moves(target, deadends, k3_new_start),
            (10 - k3_diff) + get_moves(target, deadends, k3_new_start)
        ]
        k3_moves = [x for x in k3_moves if x]
        if k3_moves:
            return min(k3_moves)

    return None


# Tests
assert get_moves(target=Combo(3, 4, 5), deadends={Combo(6, 6, 6)}) == 13
