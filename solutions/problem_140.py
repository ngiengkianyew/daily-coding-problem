def get_singles(arr):
    xored = arr[0]
    for num in arr[1:]:
        xored ^= num
    x, y = 0, 0

    rightmost_set_bit = (xored & ~(xored - 1))
    for num in arr:
        if num & rightmost_set_bit:
            x ^= num
        else:
            y ^= num

    return (x, y)


# Tests

get_singles([2, 4, 6, 8, 10, 2, 6, 10]) == (4, 8)
get_singles([2, 4, 8, 8, 10, 2, 6, 10]) == (4, 6)
