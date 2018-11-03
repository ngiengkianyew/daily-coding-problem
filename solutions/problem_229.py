import sys

SNAKES = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19,
          64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
LADDERS = {1: 38, 4: 14, 9: 31, 21: 42,
           28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
SHORCUTS = {**SNAKES, **LADDERS}
CACHE = dict()


def get_num_turns(pos, played_turns):
    if played_turns > 100 or pos > 100:
        return sys.maxsize

    if pos == 100:
        return played_turns

    if pos in CACHE:
        return CACHE[pos]

    if pos in SHORCUTS:
        num_turns = get_num_turns(SHORCUTS[pos], played_turns)
        CACHE[pos] = num_turns
        return CACHE[pos]

    possible_num_turns = list()
    for i in range(1, 7):
        num_turns = get_num_turns(pos + i, played_turns + 1)
        CACHE[pos + i] = num_turns
        possible_num_turns.append(num_turns)

    return min(possible_num_turns)


# Tests
assert get_num_turns(0, 0) == 24
