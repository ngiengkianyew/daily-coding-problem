import sys
import math


def round_list(fl_arr, int_arr, rsum, diff):
    if not fl_arr:
        return (diff, int_arr) if sum(int_arr) == rsum else (sys.maxsize, list())

    num = fl_arr[0]

    op_1 = int(math.ceil(num))
    diff_1, int_arr_1 = round_list(
        fl_arr[1:], int_arr + [op_1], rsum, diff + abs(op_1 - num))

    op_2 = int(math.floor(num))
    diff_2, int_arr_2 = round_list(
        fl_arr[1:], int_arr + [op_2], rsum, diff + abs(op_2 - num))

    return (diff_1, int_arr_1) if diff_1 < diff_2 else (diff_2, int_arr_2)


def round_list_helper(arr):
    rounded_sum = int(round(sum(arr), 0))
    return round_list(arr, list(), rounded_sum, 0)[1]


# Tests
assert round_list_helper([1.3, 2.3, 4.4]) == [1, 2, 5]
