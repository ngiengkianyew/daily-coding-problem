from typing import List


def construct_pyramid(length: int):
    assert length % 2

    peak = (length//2) + 1
    start = [x for x in range(1, peak)]
    pyramid = start + [peak] + list(reversed(start))

    return pyramid


def get_pyramid(stones: List[int]):
    len_stones = len(stones)
    len_pyr = len_stones if len_stones % 2 else len_stones - 1

    while len_pyr > 0:
        max_pyr = construct_pyramid(len_pyr)

        for offset in (0, len_stones - len_pyr):
            valid = True
            for pyr_index, pyr_num in enumerate(max_pyr):
                stone_index = pyr_index + offset
                if pyr_num > stones[stone_index]:
                    valid = False
                    break

            if valid:
                return ([0] * offset) + max_pyr + ([0] * (len_stones - offset - len_pyr))

        len_pyr -= 2

    return []


# Tests
assert get_pyramid([1, 1, 3, 3, 2, 1]) == [0, 1, 2, 3, 2, 1]
assert get_pyramid([1, 1, 1, 1, 1]) == [1, 0, 0, 0, 0]
assert get_pyramid([1, 1, 1, 5, 1]) == [0, 0, 1, 2, 1]
