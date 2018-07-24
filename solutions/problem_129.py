TOLERANCE = 10 ** -6


def almost_equal(first, second):
    # check equality with some acceptable error tolerance
    return \
        second > first - TOLERANCE and \
        second < first + TOLERANCE


def get_sqrt_helper(n, start, end):
    mid = start + ((end - start) / 2)

    if almost_equal(mid * mid, n):
        return mid
    elif mid * mid > n:
        return get_sqrt_helper(n, start, mid)
    else:
        return get_sqrt_helper(n, mid, end)


def get_sqrt(n):
    return get_sqrt_helper(n, 0, n)


assert almost_equal(get_sqrt(9), 3)
assert almost_equal(get_sqrt(2), 1.41421356237)
assert almost_equal(get_sqrt(10000), 100)
