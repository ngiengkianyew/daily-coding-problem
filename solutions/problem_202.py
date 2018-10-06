DEC_FACT = 10


def is_palindrome(num, size):
    if size == 0 or size == 1:
        return True

    fdig_factor = DEC_FACT ** (size - 1)
    fdig = num // fdig_factor
    ldig = num % DEC_FACT

    if fdig != ldig:
        return False

    new_num = (num - (fdig * fdig_factor)) // DEC_FACT
    return is_palindrome(new_num, size - 2)


def is_palindrome_helper(num):
    size = 0
    num_cp = num
    while num_cp:
        num_cp = num_cp // DEC_FACT
        size += 1

    return is_palindrome(num, size)



# Tests
assert is_palindrome_helper(121)
assert is_palindrome_helper(888)
assert not is_palindrome_helper(678)
assert not is_palindrome_helper(1678)
assert is_palindrome_helper(1661)
