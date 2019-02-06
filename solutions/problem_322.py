def jump_to_target(num):
    abs_num = abs(num)
    if abs_num < 2:
        return abs_num

    point, new_point = None, 0
    jump = 1
    while new_point <= abs_num:
        point = new_point
        new_point += jump
        jump += 1
    jump -= 2

    return (2 * (abs_num - point)) + jump


# Tests
assert jump_to_target(0) == 0
assert jump_to_target(1) == 1
assert jump_to_target(2) == 3
assert jump_to_target(3) == 2
assert jump_to_target(-3) == 2
assert jump_to_target(10) == 4
assert jump_to_target(11) == 6
