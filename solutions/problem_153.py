def get_smallest_dist(text, w1, w2):
    dist = None
    ls_word, ls_index = None, None
    for index, word in enumerate(text.split()):
        if word == w1 or word == w2:
            if (word == w1 and ls_word == w2) or \
                    (word == w2 and ls_word == w1):
                dist = index - ls_index - 1
            ls_word = word
            ls_index = index

    return dist


# Tests
assert not get_smallest_dist(
    "hello", "hello", "world")
assert get_smallest_dist(
    "hello world", "hello", "world") == 0
assert get_smallest_dist(
    "dog cat hello cat dog dog hello cat world", "hello", "world") == 1
assert get_smallest_dist(
    "dog cat hello cat dog dog hello cat world", "dog", "world") == 2
