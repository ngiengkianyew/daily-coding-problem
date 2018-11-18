def get_min_jumps(arr):
    if len(arr) < 2:
        return 0

    start = arr[0]
    candidates = list()
    for i in range(1, min(start + 1, len(arr))):
        if arr[i] == 0:
            continue
        candidate = 1 + get_min_jumps(arr[i:])
        candidates.append(candidate)

    return min(candidates)


# Tests
assert get_min_jumps([6, 2, 4, 0, 5, 1, 1, 4, 2, 9]) == 2
