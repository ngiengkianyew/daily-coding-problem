def get_max(a, b):
    c = a-b
    k = (c >> 31) & 1
    return (a - k*c)


# Tests
assert get_max(5, 3) == 5
assert get_max(5, 10) == 10
