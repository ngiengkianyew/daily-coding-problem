def is_palindrome(word):
    return word == word[::-1]


def get_unique_index_tuples(words):
    index_tuples = list()
    for i, word_i in enumerate(words):
        for j, word_j in enumerate(words):
            if i != j:
                composite = word_i + word_j
                if is_palindrome(composite):
                    index_tuples.append((i, j))

    return index_tuples


# Tests
assert get_unique_index_tuples(["code", "edoc", "da", "d"]) == [
    (0, 1), (1, 0), (2, 3)]
