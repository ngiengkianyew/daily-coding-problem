from heapq import heappush
from random import randint


def approx_median(arr):
    if not arr:
        return None

    sarr = list()
    for _ in range(len(arr)//2):
        rand = randint(0, len(arr) - 1)
    heappush(sarr, arr[rand])

    return sarr[len(sarr)//2]


# Tests
print(approx_median([3, 4, 3, 2, 4, 3, 1, 4, 3,
                     4, 2, 3, 4, 3, 0, 4, 0, 0, 1, 1, 0, 1, 2]))
