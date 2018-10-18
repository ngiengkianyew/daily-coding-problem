def get_lcos(num):
    current = longest = 0

    def reset_current():
        nonlocal current, longest
        if current > longest:
            longest = current
        current = 0

    while num:
        if num % 2:
            current += 1
        else:
            reset_current()
        num = num >> 1

    reset_current()

    return longest


# Tests
assert get_lcos(0) == 0
assert get_lcos(4) == 1
assert get_lcos(6) == 2
assert get_lcos(15) == 4
assert get_lcos(21) == 1
assert get_lcos(156) == 3
