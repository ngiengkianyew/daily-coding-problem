def get_ones(num: int):
    binary = str(bin(num))
    count = 0
    for ch in binary:
        if ch == '1':
            count += 1

    return count


def get_next(num: int):
    inc = 1
    base_count = get_ones(num)
    while True:
        next_num = num + inc
        new_count = get_ones(next_num)
        if base_count == new_count:
            return next_num
        inc += 1


# Tests
assert get_next(6) == 9
