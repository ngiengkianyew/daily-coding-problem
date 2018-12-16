import bisect


def does_element_exist(arr, x):
    pos = bisect.bisect(arr, x)
    return pos and arr[pos - 1] == x


# Tests
assert does_element_exist([1, 3, 5, 7, 9], 3)
assert not does_element_exist([1, 3, 5, 7, 9], 6)
assert does_element_exist([1, 3, 5, 7, 9], 1)
assert not does_element_exist([1, 3, 5, 7, 9], 0)
assert not does_element_exist([1, 3, 5, 7, 9], 10)
