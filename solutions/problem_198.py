def get_largest_subset(arr, prev_num=1, curr_ind=0, prev_subset=[]):
    if curr_ind == len(arr):
        return prev_subset

    curr_num = arr[curr_ind]

    alt_0 = get_largest_subset(arr, prev_num, curr_ind + 1, prev_subset)
    if curr_num % prev_num == 0:
        alt_1 = get_largest_subset(
            arr, curr_num, curr_ind + 1, prev_subset + [curr_num])
        return alt_1 if len(alt_1) > len(alt_0) else alt_0

    return alt_0


def get_largest_subset_helper(arr):
    arr.sort()
    return get_largest_subset(arr)


# Tests
assert get_largest_subset([]) == []
assert get_largest_subset([2]) == [2]
assert get_largest_subset([2, 3]) == [3]
assert get_largest_subset([3, 5, 10, 20, 21]) == [5, 10, 20]
assert get_largest_subset([1, 3, 6, 24]) == [1, 3, 6, 24]
assert get_largest_subset([3, 9, 15, 30]) == [3, 15, 30]
