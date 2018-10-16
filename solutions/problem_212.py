alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_alpha_encoding(num):
    num_chars = 1
    min_range, max_range = 1, 26
    while num > max_range:
        num_chars += 1
        min_range = max_range
        max_range += len(alphabet) ** num_chars

    chars = list()
    for _ in range(num_chars):
        interval = ((max_range - min_range + 1) // len(alphabet))
        char_pos = 0
        prev, curr = min_range, min_range + interval
        while num >= curr:
            char_pos += 1
            prev = curr
            curr = prev + interval
        chars.append(alphabet[char_pos])
        num -= prev
        min_range, max_range = prev, curr

    return "".join(chars)


# Tests
assert get_alpha_encoding(1) == "A"
assert get_alpha_encoding(20) == "T"
assert get_alpha_encoding(27) == "AA"
