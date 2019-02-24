def reduce(lst, f, init):
    res = init
    for x in lst:
        res = f(res, x)
    return res


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def custom_sum(lst):
    return reduce(lst, add, 0)


def custom_prod(lst):
    return reduce(lst, multiply, 1)


# Tests
assert custom_sum([1, 2, 3, 4]) == 10
assert custom_prod([1, 2, 3, 4]) == 24
