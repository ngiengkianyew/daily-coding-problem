def reverse_bits(num):
    inverted = list()
    for char in num:
        if char == '0':
            inverted.append('1')
        else:
            inverted.append('0')

    return "".join(inverted)


# Tests
assert reverse_bits('101') == '010'
assert reverse_bits('11110000111100001111000011110000') == \
    '00001111000011110000111100001111'
