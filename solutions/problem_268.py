def is_power_of_four(x):
    # https://stackoverflow.com/a/19611541/8650340

    return ((x & -x) & 0x55555554) == x


# Tests
assert is_power_of_four(4)
assert is_power_of_four(16)
assert is_power_of_four(64)
assert is_power_of_four(256)
assert not is_power_of_four(1)
assert not is_power_of_four(8)
assert not is_power_of_four(100)
