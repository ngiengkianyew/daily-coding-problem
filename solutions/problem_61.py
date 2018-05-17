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
        result *= result
        prev_pow = current_pow
        current_pow *= 2

    if prev_pow:
        prev_result *= pow(x, y - prev_pow)

    return 1/prev_result if y != y_abs else prev_result


assert pow(2, 2) == 4
assert pow(2, 10) == 1024
assert pow(2, 1) == 2
assert pow(3, 3) == 27
assert pow(10, 3) == 1000
