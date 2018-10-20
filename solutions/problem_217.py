def get_next_sparse(num):
    str_bin = str(bin(num))[2:]

    new_str_bin = ""
    prev_digit = None
    flag = False
    for i, digit in enumerate(str_bin):
        if digit == '1' and prev_digit == '1':
            flag = True

        if flag:
            new_str_bin += '0' * (len(str_bin) - i)
            break
        else:
            new_str_bin += digit
        prev_digit = digit

    if flag:
        if new_str_bin[0] == '1':
            new_str_bin = '10' + new_str_bin[1:]
        else:
            new_str_bin = '1' + new_str_bin

    new_num = int(new_str_bin, base=2)

    return new_num


# Tests
assert get_next_sparse(21) == 21
assert get_next_sparse(25) == 32
assert get_next_sparse(255) == 256
