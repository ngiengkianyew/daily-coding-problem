def pow(x, y):
    if not x:
        return 0
    elif not y:
        return 1

    y_abs = abs(y)

    current_pow = 1
    prev_result, prev_pow = 0, 0
    result = x
    while current_pow <= y_abs:
        prev_result = result
        prev_pow = current_pow
        result *= result
        current_pow *= 2

    prev_result *= pow(x, y_abs - prev_pow)

    return 1/prev_result if y != y_abs else prev_result


assert pow(2, 2) == 4
assert pow(2, 10) == 1024
assert pow(2, 1) == 2
assert pow(3, 3) == 27
assert pow(10, 3) == 1000
assert pow(2, -3) == 0.125
assert pow(10, -2) == 0.01
assert pow(5, 0) == 1
assert pow(0, 2) == 0
