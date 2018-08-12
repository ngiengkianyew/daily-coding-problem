def get_gray_code(n):
    """
    n: bits 
    """
    if n == 0:
        return ['']

    lower_grey_codes = get_gray_code(n - 1)
    l0 = ['0' + x for x in lower_grey_codes]
    l1 = ['1' + x for x in reversed(lower_grey_codes)]

    return l0 + l1


# Tests
assert get_gray_code(1) == ['0', '1']
assert get_gray_code(2) == ['00', '01', '11', '10']
assert get_gray_code(3) == ['000', '001', '011',
                            '010', '110', '111', '101', '100']
assert get_gray_code(4) == ['0000', '0001', '0011', '0010', '0110', '0111',
                            '0101', '0100', '1100', '1101', '1111', '1110', '1010', '1011', '1001', '1000']
