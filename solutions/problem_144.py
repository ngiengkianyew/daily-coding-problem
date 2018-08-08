def get_mapping_indices(arr):
    nl_indices = dict()
    sorted_tuples = [(x, i) for i, x in enumerate(arr)]
    sorted_tuples.sort(key=lambda x: x[0])

    for k, (_, i) in enumerate(sorted_tuples[:-1]):
        min_dist = len(arr)
        for m in range(k + 1, len(sorted_tuples)):
            dist = abs(i - sorted_tuples[m][1])
            if dist < min_dist:
                min_dist = dist
                nl_indices[i] = sorted_tuples[m][1]

    return nl_indices


def nearest_larger(arr, index):
    nl_indices = get_mapping_indices(arr)

    if index not in nl_indices:
        return None

    return nl_indices[index]


# Tests
assert nearest_larger([4, 1, 3, 5, 6], 0) == 3
assert nearest_larger([4, 1, 3, 5, 6], 1) == 0 or \
    nearest_larger([4, 1, 3, 5, 6], 1) == 2
assert not nearest_larger([4, 1, 3, 5, 6], 4)
assert nearest_larger([4, 1, 3, 5, 6], 3) == 4
