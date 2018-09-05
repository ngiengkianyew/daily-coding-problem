from itertools import permutations


def get_indices(s, words):
    perms = list(permutations(words))
    perms = [x + y for (x, y) in perms]

    indices = [s.find(x) for x in perms]
    indices = [x for x in indices if x >= 0]

    return sorted(indices)


# Tests
assert get_indices("dogcatcatcodecatdog", ["cat", "dog"]) == [0, 13]
assert not get_indices("barfoobazbitbyte", ["cat", "dog"])
