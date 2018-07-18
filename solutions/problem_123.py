def strip_neg(num):
    if num[0] != '-':
        return num
    elif len(num) > 1:
        return num[1:]


def is_valid_number_helper(string, dec):
    if not string:
        return True

    char = string[0]
    if (dec and char == '.') or (not char.isdigit() and char != '.'):
        return False
    elif char == '.':
        dec = True

    return is_valid_number_helper(string[1:], dec)


def is_valid_number(string):
    if not string:
        return False

    split_list = string.split('e')
    if len(split_list) > 2:
        return False

    if len(split_list) == 2:
        string_1 = strip_neg(split_list[0])
        string_2 = strip_neg(split_list[1])
        return string_1 and string_2 and \
            is_valid_number_helper(string_1, False) and \
            is_valid_number_helper(string_2, False)
    else:
        string = strip_neg(split_list[0])
        return string and is_valid_number_helper(string, False)


# Tests
assert is_valid_number("10")
assert is_valid_number("-10")
assert is_valid_number("10.1")
assert is_valid_number("-10.1")
assert is_valid_number("1e5")
assert is_valid_number("-5")
assert is_valid_number("1e-5")
assert is_valid_number("1e-5.2")
assert not is_valid_number("a")
assert not is_valid_number("x 1")
assert not is_valid_number("a -2")
assert not is_valid_number("-")
