def get_occurrences(string, pattern):
    sl, pl = len(string), len(pattern)
    occurrences = list()

    for i in range(sl - pl + 1):
        if string[i:i+pl] == pattern:
            occurrences.append(i)

    return occurrences


# Tests
assert get_occurrences("abracadabra", "abr") == [0, 7]
assert not get_occurrences("abracadabra", "xyz")
assert not get_occurrences("abr", "abracadabra")
assert get_occurrences("aaaa", "aa") == [0, 1, 2]
