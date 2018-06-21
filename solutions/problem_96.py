def get_permutations(arr):
    if len(arr) < 2:
        return [arr]

    permutations = list()
    for i, num in enumerate(arr):
        arr_cp = arr[:i] + arr[i+1:]
        child_perms = get_permutations(arr_cp)
        for perm in child_perms:
            permutations.append([num] + perm)

    return permutations


assert get_permutations([]) == [[]]
assert get_permutations([1]) == [[1]]
assert get_permutations([1, 2]) == [[1, 2], [2, 1]]
assert get_permutations([1, 2, 3]) == \
    [[1, 2, 3], [1, 3, 2], [2, 1, 3],
     [2, 3, 1], [3, 1, 2], [3, 2, 1]]
