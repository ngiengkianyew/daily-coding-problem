values = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}


def convert_roman_to_decimal(roman):
    if not roman:
        return 0

    pchar = roman[-1]
    decimal = values[pchar]
    for char in reversed(roman[:-1]):
        decimal += values[char] * (-1 if values[char] < values[pchar] else 1)
        pchar = char

    return decimal


# Tests
assert convert_roman_to_decimal("I") == 1
assert convert_roman_to_decimal("IV") == 4
assert convert_roman_to_decimal("XL") == 40
assert convert_roman_to_decimal("XIV") == 14
