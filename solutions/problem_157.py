def check_palindrome_rearrangement(string):
    chars = set()
    for char in string:
        if char not in chars:
            chars.add(char)
        else:
            chars.remove(char)

    return len(chars) < 2


# Tests
assert check_palindrome_rearrangement("carrace")
assert not check_palindrome_rearrangement("daily")
assert not check_palindrome_rearrangement("abac")
assert check_palindrome_rearrangement("abacc")
assert check_palindrome_rearrangement("aabb")
assert not check_palindrome_rearrangement("aabbcccd")
