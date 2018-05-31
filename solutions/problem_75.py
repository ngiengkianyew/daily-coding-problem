cache = None


def get_subseq(arr, start):
    if start == len(arr):
        return 0

    current = arr[start]
    max_inc = 1
    for index in range(start + 1, len(arr)):
        if arr[index] >= current:
            if index in cache:
                count = cache[index]
            else:
                count = get_subseq(arr, index) + 1
                cache[index] = count
            if count > max_inc:
                max_inc = count

    return max_inc


def get_subseq_helper(arr):
    global cache
    cache = dict()
    return get_subseq(arr, 0)


assert get_subseq_helper([]) == 0
assert get_subseq_helper([0, 1]) == 2
assert get_subseq_helper([0, 2, 1]) == 2
assert get_subseq_helper([0, 1, 2]) == 3
assert get_subseq_helper([2, 1, 0]) == 1
assert get_subseq_helper(
    [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 6
