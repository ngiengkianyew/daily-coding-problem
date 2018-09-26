def end_reachable(arr):
    if len(arr) < 2:
        return True

    for i in range(2, len(arr) + 1):
        if arr[len(arr) - i] >= i - 1:
            return end_reachable(arr[:len(arr) - i + 1])


# Tests
assert end_reachable([1, 3, 1, 2, 0, 1])
assert not end_reachable([1, 2, 1, 0, 0])
