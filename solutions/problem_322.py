def jump_to_target(num):
    abs_num = abs(num)
    if abs_num < 2:
        return abs_num

    return 1 + (2 * (abs_num - 1))


# Tests
assert jump_to_target(0) == 0
assert jump_to_target(1) == 1
assert jump_to_target(2) == 3
assert jump_to_target(3) == 5
assert jump_to_target(-3) == 5
