# Solution 1
def rotate_list_once(arr):
    first = arr[0]
    for i in range(len(arr) - 1):
        arr[i] = arr[i + 1]
    arr[-1] = first
    return arr


def rotate_list(arr, k):
    for _ in range(k):
        arr = rotate_list_once(arr)

    return arr


# Solution 2
def rotate_list_alt(arr, k):
    return arr[k:] + arr[:k]


# Tests
assert rotate_list([1, 2, 3, 4, 5, 6], 0) == [1, 2, 3, 4, 5, 6]
assert rotate_list_alt([1, 2, 3, 4, 5, 6], 0) == [1, 2, 3, 4, 5, 6]

assert rotate_list([1, 2, 3, 4, 5, 6], 2) == [3, 4, 5, 6, 1, 2]
assert rotate_list_alt([1, 2, 3, 4, 5, 6], 2) == [3, 4, 5, 6, 1, 2]

assert rotate_list([1, 2, 3, 4, 5, 6], 4) == [5, 6, 1, 2, 3, 4]
assert rotate_list_alt([1, 2, 3, 4, 5, 6], 4) == [5, 6, 1, 2, 3, 4]
