KAP_CONST = 6174


def apply_kproc(num, steps=0):
    if num == KAP_CONST:
        return steps

    digits = str(num)
    assert len(set(digits)) > 2

    asc_num = "".join(sorted(digits))
    dsc_num = "".join(sorted(digits, reverse=True))

    diff = int(dsc_num) - int(asc_num)
    return apply_kproc(diff, steps + 1)


# Tests
assert apply_kproc(KAP_CONST) == 0
assert apply_kproc(1234) == 3
