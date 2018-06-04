def can_edit(arr):
    decr_pairs = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            decr_pairs += 1

    return decr_pairs <= 1


assert can_edit([10, 5, 7])
assert not can_edit([10, 5, 1])
assert can_edit([1, 10, 5, 7])

