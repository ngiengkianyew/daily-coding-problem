from typing import List


def get_ways_to_produce(num: int, factors: List[int]):
    if not num or num in factors:
        return 1

    ways = 0
    for i, factor in enumerate(factors):
        if num % factor == 0:
            ways += get_ways_to_produce(num // factor, factors[i:])

    return ways


def get_denominators(ways_to_produce: List[int]):
    factors = [i for i, num in enumerate(ways_to_produce)
               if (num == 1 and i > 0)]

    for i, num in enumerate(ways_to_produce):
        if get_ways_to_produce(i, factors) == num - 1:
            factors.append(i)

    return factors


# Tests
assert get_denominators([1, 0, 1, 1, 2]) == [2, 3, 4]
