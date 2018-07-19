from math import log, ceil


def get_num_expected(coin_tosses):
    return ceil(log(coin_tosses, 2))


assert get_num_expected(1) == 0
assert get_num_expected(2) == 1
assert get_num_expected(100) == 7
assert get_num_expected(200) == 8
