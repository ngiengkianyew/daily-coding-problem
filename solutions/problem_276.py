def contains_pattern(string, pattern):
    if not string or not pattern:
        return False

    slen, plen = len(string), len(pattern)
    if plen > len(string):
        return False

    hashed_strings = set()
    for i in range(slen - plen + 1):
        hashed_strings.add(string[i:i+plen])

    return pattern in hashed_strings


# Tests
assert contains_pattern("abcabcabcd", "abcd")
assert not contains_pattern("abcabcabc", "abcd")
