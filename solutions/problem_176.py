def is_char_mapped(str_a, str_b):
    if len(str_a) != len(str_b):
        return False

    char_map = dict()
    for char_a, char_b in zip(str_a, str_b):
        if char_a not in char_map:
            char_map[char_a] = char_b
        elif char_map[char_a] != char_b:
            return False

    return True


# Tests
assert is_char_mapped("abc", "bcd")
assert not is_char_mapped("foo", "bar")
