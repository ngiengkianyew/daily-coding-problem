def get_perfect_number(n):
    tmp_sum = 0
    for char in str(n):
        tmp_sum += int(char)

    return (n * 10) + (10 - tmp_sum)


assert get_perfect_number(1) == 19
assert get_perfect_number(2) == 28
assert get_perfect_number(3) == 37
assert get_perfect_number(10) == 109
assert get_perfect_number(11) == 118
assert get_perfect_number(19) == 190
