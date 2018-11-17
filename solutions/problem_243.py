import sys


def split(arr, k):
    if k == 1:
        return ([arr], sum(arr))

    min_val = sys.maxsize
    min_cand = None
    for i in range(len(arr)):
        arr_1, sum_1 = ([arr[:i]], sum(arr[:i]))
        arr_2, sum_2 = split(arr[i:], k - 1)
        candidate = arr_1 + arr_2, max(sum_1, sum_2)
        if candidate[1] < min_val:
            min_val = candidate[1]
            min_cand = candidate

    return min_cand


def split_helper(arr, k):
    return split(arr, k)[1]


# Tests
assert split_helper([5, 1, 2, 7, 3, 4], 3) == 8
