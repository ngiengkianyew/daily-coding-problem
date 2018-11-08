class Trie:
    def __init__(self):
        self.size = 0
        self.value = 0
        self.letter_map = dict()

    def __repr__(self):
        return "{}: {}".format(self.letter_map, self.value)

    def add_word(self, word, value):
        if not word:
            self.value += value
            return
        letter = word[0]

        sub_trie = None
        if letter in self.letter_map:
            sub_trie = self.letter_map[letter]
        else:
            sub_trie = Trie()
            self.letter_map[letter] = sub_trie

        self.size += 1
        sub_trie.add_word(word[1:], value)
        self.value = sum([x.value for x in self.letter_map.values()])

    def find_prefix(self, word):
        if not word:
            return self.value

        letter = word[0]
        if letter in self.letter_map:
            sub_trie = self.letter_map[letter]
            return sub_trie.find_prefix(word[1:])

        return 0


class PrefixMapSum:

    def __init__(self, trie):
        self.trie = trie

    def insert(self, key, value):
        self.trie.add_word(key, value)

    def sum(self, prefix):
        return self.trie.find_prefix(prefix)


# Tests
pms = PrefixMapSum(Trie())
pms.insert("columnar", 3)
assert pms.sum("col") == 3
pms.insert("column", 2)
assert pms.sum("col") == 5
