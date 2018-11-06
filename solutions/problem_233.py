def get_fib(n):
    assert n > 0

    fib_a = 0
    fib_b = 1

    if n == 1:
        return fib_a
    elif n == 2:
        return fib_b

    fib_c = None
    for _ in range(n - 2):
        fib_c = fib_a + fib_b
        fib_a = fib_b
        fib_b = fib_c

    return fib_c


## Tests
assert get_fib(5) == 3
assert get_fib(2) == 1
assert get_fib(7) == 8
