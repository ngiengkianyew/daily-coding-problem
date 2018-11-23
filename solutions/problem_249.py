import sys


def max_xor(arr):
    maxx = -sys.maxsize
    for i in range(len(arr) - 1):
        for k in range(i + 1, len(arr)):
            maxx = max(maxx, arr[i] ^ arr[k])

    return maxx


# Tests
assert max_xor([1, 2, 3, 4]) == 7
