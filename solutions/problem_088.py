def divide(dividend, divisor):
    if not divisor:
        return

    current_sum = 0
    quotient = 0
    while current_sum <= dividend:
        quotient += 1
        current_sum += divisor

    return quotient - 1


assert not divide(1, 0)
assert divide(1, 1) == 1
assert divide(0, 1) == 0
assert divide(12, 3) == 4
assert divide(13, 3) == 4
assert divide(25, 5) == 5
assert divide(25, 7) == 3
