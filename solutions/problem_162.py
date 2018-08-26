class Trie:
    def __init__(self):
        self.size = 0
        self.letter_map = dict()

    def __repr__(self):
        return str(self.letter_map)

    def add_word(self, word):
        if not word:
            return
        letter = word[0]

        sub_trie = None
        if letter in self.letter_map:
            sub_trie = self.letter_map[letter]
        else:
            sub_trie = Trie()
            self.letter_map[letter] = sub_trie

        self.size += 1
        sub_trie.add_word(word[1:])

    def get_sup(self, word, prev):
        # get shortest unique prefix
        if self.size < 2:
            return prev

        letter = word[0]
        sub_trie = self.letter_map[letter]
        return sub_trie.get_sup(word[1:], prev + letter)


def get_sups(words):
    trie = Trie()
    for word in words:
        trie.add_word(word)

    sups = list()
    for word in words:
        sups.append(trie.get_sup(word, ""))

    return sups


# Tests
assert get_sups(["dog", "cat", "apple", "apricot", "fish"]) == \
    ["d", "c", "app", "apr", "f"]
