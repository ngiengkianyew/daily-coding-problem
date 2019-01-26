def get_arrangement_count(free_spaces):
    if not free_spaces:
        return 1
    elif free_spaces < 2:
        return 0

    arrangements = 0
    if free_spaces >= 3:
        arrangements += (2 + get_arrangement_count(free_spaces - 3))
    arrangements += (2 + get_arrangement_count(free_spaces - 2))

    return arrangements


def count_arragements(columns):
    return get_arrangement_count(columns * 2)


# Tests
assert count_arragements(4) == 32
