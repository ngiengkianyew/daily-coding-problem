def get_num(x, y, b):
    return x * b + y * abs(b-1)


assert get_num(3, 4, 1) == 3
assert get_num(3, 4, 0) == 4
