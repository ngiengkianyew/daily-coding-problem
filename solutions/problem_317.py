# if there are 2 consecutive numbers, the least significant
# bit will be 0 once, which means the result of an AND on
# the last bit will be zero
from math import log2, ceil


def bitwise_and_slow(start, end):
    result = end
    for num in range(start, end):
        result &= num

    return result


def bitwise_and(start, end):
    diff = end - start + 1
    power_diff = ceil(log2(diff))
    power_end = ceil(log2(end))

    result = start & (2**power_end - 2**power_diff)
    return result


# Tests
assert bitwise_and_slow(5, 6) == 4
assert bitwise_and(5, 6) == 4
assert bitwise_and_slow(126, 127) == 126
assert bitwise_and(126, 127) == 126
assert bitwise_and_slow(129, 215) == 128
assert bitwise_and(193, 215) == 192
