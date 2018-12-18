def get_fixed_point(arr):
    for i, num in enumerate(arr):
        if i == num:
            return i

    return False


# Tests
assert get_fixed_point([-6, 0, 2, 40]) == 2
assert get_fixed_point([1, 5, 7, 8]) == False
