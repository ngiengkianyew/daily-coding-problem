def get_max_hist_area(arr, start, end):
    if start == end:
        return 0

    curr_area = (end - start) * min(arr[start:end])
    opt_1 = get_max_hist_area(arr, start, end - 1)
    opt_2 = get_max_hist_area(arr, start + 1, end)

    return max(curr_area, opt_1, opt_2)


def get_max_hist_area_helper(arr):
    return get_max_hist_area(arr, 0, len(arr))


# Tests
assert get_max_hist_area_helper([1, 3, 2, 5]) == 6
