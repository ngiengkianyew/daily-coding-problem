def encode_string(s):
    encoded_chars = list()

    count = 0
    prev_char = None
    for char in s:
        if char == prev_char or not prev_char:
            count += 1
        else:
            encoded_chars.append(str(count))
            encoded_chars.append(prev_char)
            count = 1
        prev_char = char

    if count:
        encoded_chars.append(str(count))
        encoded_chars.append(prev_char)

    return "".join(encoded_chars)


def decode_string(s):

    decoded_chars = list()
    index = 0

    while index < len(s):
        decoded_chars.append(int(s[index]) * s[index + 1])
        index += 2

    return "".join(decoded_chars)


assert encode_string("") == ""
assert encode_string("AAA") == "3A"
assert encode_string("AAAABBBCCDAA") == "4A3B2C1D2A"

assert decode_string("") == ""
assert decode_string("3A") == "AAA"
assert decode_string("4A3B2C1D2A") == "AAAABBBCCDAA"
