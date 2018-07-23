def get_sentence_split(s, words):
    if not s or not words:
        return []

    word_set = set(words)
    sentence_words = list()
    for i in range(len(s)):
        if s[0:i + 1] in word_set:
            sentence_words.append(s[0:i + 1])
            word_set.remove(s[0:i + 1])
            sentence_words += get_sentence_split(s[i + 1:], word_set)
            break

    return sentence_words


assert get_sentence_split("thequickbrownfox", ['quick', 'brown', 'the', 'fox']) == [
    'the', 'quick', 'brown', 'fox']
assert get_sentence_split("bedbathandbeyond", [
                          'bed', 'bath', 'bedbath', 'and', 'beyond']) == ['bed', 'bath', 'and', 'beyond']
