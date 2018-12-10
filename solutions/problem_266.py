ALPHA_SIZE = 26
APLHA_ASCII_OFFSET = 65


class WordCode:
    def __init__(self, word):
        self.word = word
        self.vec = [0 for _ in range(ALPHA_SIZE)]
        for ch in word:
            ind = ord(ch) - APLHA_ASCII_OFFSET
            self.vec[ind] += 1

    def __repr__(self):
        return "{}=>{}".format(self.word, self.vec)

    def __sub__(self, other):
        result = list()
        for i in range(ALPHA_SIZE):
            result.append(max(0, self.vec[i] - other.vec[i]))

        return result


def get_step_words(word, dictionary):
    step_words = set()
    wc = WordCode(word)
    for dword in dictionary:
        dwc = WordCode(dword)
        diff = dwc - wc
        if sum(diff) == 1:
            step_words.add(dword)

    return step_words


# Tests
assert get_step_words("APPLE", {"APPEAL"}) == {"APPEAL"}
assert get_step_words("APPLE", {"APPEAL", "APPLICT"}) == {"APPEAL"}
assert get_step_words("APPLE", {"APPEAL", "APPLICT", "APPLES"}) == {"APPEAL", "APPLES"}
