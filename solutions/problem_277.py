BLEN = 8
SHIFT_RES = {
    2: 6,
    3: 14,
    4: 30
}
TAIL_SHIFT = 6
TAIL_SHIFT_RES = 2


def is_valid_utf8(int_arr):
    ln = len(int_arr)
    if ln == 1:
        return int_arr[0] < 128

    first = int_arr[0]
    tail = int_arr[1:]

    sfirst = first >> (BLEN - ln - 1)
    if SHIFT_RES[ln] != sfirst:
        return False

    for num in tail:
        snum = num >> TAIL_SHIFT
        if snum != TAIL_SHIFT_RES:
            return False

    return True


# Tests
assert is_valid_utf8([226, 130, 172])
assert not is_valid_utf8([226, 194, 172])
assert not is_valid_utf8([226])
assert is_valid_utf8([100])
assert is_valid_utf8([194, 130])
