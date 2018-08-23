def get_first_recurring(string):
    seen = set()
    for char in string:
        if char in seen:
            return char
        seen.add(char)

    return None


# Tests
assert get_first_recurring("acbbac") == "b"
assert not get_first_recurring("abcdef")
