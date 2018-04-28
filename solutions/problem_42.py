def get_subset_for_sum(arr, k):

    if len(arr) == 0:
        return None

    if arr[0] == k:
        return [arr[0]]

    with_first = get_subset_for_sum(arr[1:], k - arr[0])
    if with_first:
        return [arr[0]] + with_first
    else:
        return get_subset_for_sum(arr[1:], k)


assert not get_subset_for_sum([], 1)
assert get_subset_for_sum([12, 1, 61, 5, 9, 2], 24) == [12, 1, 9, 2]
assert get_subset_for_sum([12, 1, 61, 5, 9, 2], 61) == [61]
assert get_subset_for_sum([12, 1, 61, 5, -108, 2], -106) == [-108, 2]
