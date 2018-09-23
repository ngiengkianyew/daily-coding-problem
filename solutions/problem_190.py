def get_max_circ_sarray(arr):
    warr = arr * 2

    items = []
    csum = msum = 0

    for num in warr:
        while len(items) >= len(arr) or (items and items[0] < 1):
            csum -= items[0]
            items = items[1:]

        items.append(num)
        csum += num

        msum = max(msum, csum)

    return msum


# Tests
assert get_max_circ_sarray([8, -1, 3, 4]) == 15
assert get_max_circ_sarray([-4, 5, 1, 0]) == 6
