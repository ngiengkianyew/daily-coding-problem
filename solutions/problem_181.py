def is_palindrome(string):
    return string and string == string[::-1]


def split_into_pals(string, curr="", prev_pals=[]):
    # print("string: {}, curr: {}, prev_pals: {}".format(string, curr, prev_pals))

    if not string and not curr:
        return prev_pals
    elif not string:
        return prev_pals + list(curr)

    candidate = curr + string[0]

    alt_1 = []
    if is_palindrome(candidate):
        alt_1 = split_into_pals(string[1:], "", prev_pals + [candidate])
    alt_2 = split_into_pals(string[1:], candidate, prev_pals)

    if alt_1 and alt_2:
        return alt_2 if len(alt_2) < len(alt_1) else alt_1

    return alt_2


# Tests
assert split_into_pals("racecarannakayak") == ["racecar", "anna", "kayak"]
assert split_into_pals("abc") == ["a", "b", "c"]
