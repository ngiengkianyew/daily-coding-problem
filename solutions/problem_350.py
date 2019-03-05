import sys


def get_sum_sq(target, squares):
    if target == 0:
        return 0
    elif not squares:
        return sys.maxsize

    original_tgt = target
    biggest_sq = squares.pop()
    tally = 0
    while target >= biggest_sq:
        tally += 1
        target -= biggest_sq

    if tally:
        return min(
            tally + get_sum_sq(target, squares.copy()),
            get_sum_sq(original_tgt, squares.copy())
        )
    else:
        return get_sum_sq(original_tgt, squares.copy())


def get_min_squares(target):
    num, sq = 1, 1
    squares = list()
    while sq <= target:
        squares.append(sq)
        num += 1
        sq = num * num

    return get_sum_sq(target, squares)


# Tests
assert get_min_squares(4) == 1
assert get_min_squares(17) == 2
assert get_min_squares(18) == 2
