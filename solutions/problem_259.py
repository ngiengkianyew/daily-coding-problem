def get_optimal_chars(words):
    candidates = dict()
    for word in words:
        fc = word[0]
        if fc not in candidates:
            candidates[fc] = set()
        candidates[fc].add(len(word))

    opt_chars = set()
    for char in candidates:
        if all((not (x % 2)) for x in candidates[char]):
            opt_chars.add(char)

    return opt_chars


# Tests
assert get_optimal_chars(["cat", "calf", "dog", "bear"]) == set(['b'])
assert get_optimal_chars(["cat", "calf", "dog", "bear", "ao"]) == set(['b', 'a'])
