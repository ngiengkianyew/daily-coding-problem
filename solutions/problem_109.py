# 85 is the odd-bit filter '01010101'


def swap_bits(num):
    return ((num & 85) << 1) | ((num & (85 << 1)) >> 1)


assert swap_bits(0) == 0
assert swap_bits(255) == 255
assert swap_bits(210) == 225
assert swap_bits(170) == 85
assert swap_bits(226) == 209
