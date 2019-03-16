def get_strob_numbers(num_digits):
    if not num_digits:
        return [""]
    elif num_digits == 1:
        return ["0", "1", "8"]

    smaller_strob_numbers = get_strob_numbers(num_digits - 2)
    strob_numbers = list()
    for x in smaller_strob_numbers:
        strob_numbers.extend([
            "1" + x + "1",
            "6" + x + "9",
            "9" + x + "6",
            "8" + x + "8",
        ])

    return strob_numbers


# Tests
assert get_strob_numbers(1) == ['0', '1', '8']
assert get_strob_numbers(2) == ['11', '69', '96', '88']
assert get_strob_numbers(3) == ['101', '609', '906', '808', '111', '619',
                                '916', '818', '181', '689', '986', '888']
