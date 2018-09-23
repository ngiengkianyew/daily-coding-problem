def get_max_subarray(arr):
    csum = msum = 0
    for num in arr:
        csum = max(csum + num, num)
        msum = max(csum, msum)

    return msum


def get_max_circ_sarray(arr):
    warr = arr * 2
    return max(get_max_subarray(warr[i:i+len(arr)]) for i in range(len(arr)))


# Tests
assert get_max_circ_sarray([8, -1, 3, 4]) == 15
assert get_max_circ_sarray([-4, 5, 1, 0]) == 6
