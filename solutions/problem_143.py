def swap_indices(arr, i, k):
    tmp = arr[i]
    arr[i] = arr[k]
    arr[k] = tmp


def separate_with_pivot(arr, i, k, x):
    if not arr:
        return

    while i < k:
        if arr[i] >= x and arr[k] < x:
            swap_indices(arr, i, k)
        else:
            if arr[i] < x:
                i += 1
            if arr[k] >= x:
                k -= 1

    return i + 1 if (arr[i] < x and i + 1 < len(arr)) else i


def pivot_list(arr, x):
    mid = separate_with_pivot(arr, 0, len(arr) - 1, x)
    separate_with_pivot(arr, mid, len(arr) - 1, x + 1)

    return arr



# Tests
assert pivot_list([9, 12, 3, 5, 14, 10, 10], 10) == [9, 5, 3, 10, 10, 14, 12]
assert pivot_list([9, 12, 3, 5, 14, 10, 10], 8) == [5, 3, 12, 9, 14, 10, 10]
assert pivot_list([9, 12, 14, 10, 10], 8) == [9, 12, 14, 10, 10]
assert pivot_list([3, 5], 8) == [3, 5]
assert pivot_list([8, 8, 8], 8) == [8, 8, 8]
assert pivot_list([], 8) == []
