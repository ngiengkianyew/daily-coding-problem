def get_closest_factors(num):
    a, b = 1, num
    pa, pb = 1, 1
    while b > a:
        if num % a == 0:
            pa, pb = a, num // a
        b = num / a
        a += 1

    return (pa, pb)


def reduce(num):
    if num == 1:
        return [1]

    # permitted step 1
    next_steps = reduce(num - 1)

    # permitted step 2
    _, large_factor = get_closest_factors(num)
    if large_factor < num:
        # only consider this option if the number is not a prime
        alt_2 = reduce(large_factor)
        if len(next_steps) > len(alt_2):
            # if it's a better option that decrementing by 1, use it
            next_steps = alt_2

    return [num] + next_steps


# Tests
assert reduce(100) == [100, 10, 9, 3, 2, 1]
assert reduce(50) == [50, 10, 9, 3, 2, 1]
assert reduce(64) == [64, 8, 4, 2, 1]
assert reduce(31) == [31, 30, 6, 3, 2, 1]
