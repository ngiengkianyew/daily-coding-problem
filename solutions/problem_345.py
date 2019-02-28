def get_synonyms(pairs):
    synonyms = dict()
    for pair in pairs:
        default = min(pair)
        synonyms[pair[0]] = default
        synonyms[pair[1]] = default

    return synonyms


def are_equal(s1, s2, synonyms):
    words_1, words_2 = s1.split(), s2.split()
    if len(words_1) != len(words_2):
        return False

    def lookup(word):
        return synonyms[word] if word in synonyms else word

    for (w1, w2) in zip(words_1, words_2):
        a1 = lookup(w1)
        a2 = lookup(w2)
        if a1 != a2:
            return False

    return True


# Tests
synonyms = get_synonyms([("big", "large"), ("eat", "consume")])
assert are_equal("He wants to eat food.",
                 "He wants to consume food.",
                 synonyms)
assert not are_equal("He wants to large food.",
                     "He wants to consume food.",
                     synonyms)
