def permute(arr, perms):
    evicted = dict()
    for i, (num, new_pos) in enumerate(zip(arr, perms)):
        if i in evicted:
            num = evicted[i]
            del evicted[i]

        if new_pos > i:
            evicted[new_pos] = arr[new_pos]

        arr[new_pos] = num

    return arr


# Tests
assert permute(['a', 'b', 'c'], [2, 1, 0]) == ['c', 'b', 'a']
assert permute(['a', 'b', 'c', 'd'], [2, 1, 0, 3]) == ['c', 'b', 'a', 'd']
assert permute(['a', 'b', 'c', 'd'], [3, 0, 1, 2]) == ['b', 'c', 'd', 'a']
