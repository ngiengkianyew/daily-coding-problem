def find_duplicate(arr, n):
    expected_sum = int((n * (n+1)) / 2)
    actual_sum = sum(arr)

    return actual_sum - expected_sum


# Tests

assert find_duplicate([1, 1, 2], 2) == 1
assert find_duplicate([1, 2, 3, 3], 3) == 3
assert find_duplicate([1, 2, 3, 4, 3], 4) == 3
