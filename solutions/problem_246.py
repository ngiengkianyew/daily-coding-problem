def can_form_circle(curr_char, remaining_words, seen_circle, word_dict):
    if not remaining_words and curr_char == seen_circle[0][0]:
        print(seen_circle + [seen_circle[0]])
        return True

    if curr_char not in word_dict or not word_dict[curr_char]:
        return False

    next_words = word_dict[curr_char].copy()
    for next_word in next_words:
        word_dict_cp = word_dict.copy()
        word_dict_cp[curr_char].remove(next_word)
        if can_form_circle(next_word[-1], remaining_words - {next_word},
                           seen_circle + [next_word], word_dict_cp):
            return True

    return False


def create_word_dict(words):
    word_dict = dict()
    for word in words:
        start_char = word[0]
        if not start_char in word_dict:
            word_dict[start_char] = set()
        word_dict[start_char].add(word)
    return word_dict


def circle_helper(words):
    words = set(words)
    word_dict = create_word_dict(words)
    for word in words:
        curr_char = word[-1]
        if can_form_circle(curr_char, words - {word}, [word], word_dict):
            return True

    return False


# Tests
assert circle_helper(['chair', 'height', 'racket', 'touch', 'tunic'])
assert not circle_helper(['height', 'racket', 'touch', 'tunic'])
assert circle_helper(['abc', 'cba'])
