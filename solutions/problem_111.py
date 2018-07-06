def add_needed_char(needed, char):
    if char not in needed:
        needed[char] = 0
    needed[char] += 1


def remove_gained_char(needed, char):
    needed[char] -= 1


def get_anagram_starts(string, word):
    if len(word) > len(string):
        return []

    anagram_indices = list()
    charset = set(word)

    needed = dict()
    for i, char_needed in enumerate(word):
        add_needed_char(needed, char_needed)

    for i in range(len(word)):
        char_gained = string[i]
        remove_gained_char(needed, char_gained)

    # This is a constant time operation because it has
    # a fixed upper bound of 26 read operations
    if all([x < 1 for x in needed.values()]):
        anagram_indices.append(0)

    for i in range(len(word), len(string)):
        window_start = i - len(word)
        char_removed = string[window_start]
        char_gained = string[i]

        if char_removed in charset:
            add_needed_char(needed, char_removed)

        if char_gained in needed:
            remove_gained_char(needed, char_gained)

        if all([x < 1 for x in needed.values()]):
            anagram_indices.append(window_start + 1)

    return anagram_indices


# Tests
assert get_anagram_starts("abxaba", "ab") == [0, 3, 4]
assert get_anagram_starts("cataract", "tac") == [0, 5]
