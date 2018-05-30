def get_mult_count(n, x):
    if n == 1:
        return n

    tuples = list()
    for i in range(1, (x + 1) // 2):
        if not x % i:
            tuples.append((i, x // i))

    return len(tuples)


assert get_mult_count(1, 1) == 1
assert get_mult_count(6, 12) == 4
assert get_mult_count(2, 4) == 1
assert get_mult_count(3, 6) == 2
