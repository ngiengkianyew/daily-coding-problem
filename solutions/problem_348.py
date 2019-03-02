class TernaryTree:
    def __init__(self):
        self.ch = None
        self.l = None
        self.m = None
        self.r = None

    def __repr__(self):
        return "{}->[{}-{}-{}]".format(
            self.ch if self.ch else "",
            self.m if self.m else "",
            self.l if self.l else "",
            self.r if self.r else "")

    @staticmethod
    def add_tree(loc, word):
        if not loc:
            loc = TernaryTree()
        loc.add_word(word)
        return loc

    def add_word(self, word):
        if not word:
            return
        fch = word[0]
        rem_word = word[1:]

        if not self.ch:
            self.ch = fch
            self.m = TernaryTree.add_tree(self.m, rem_word)
        elif self.ch == fch:
            self.m = TernaryTree.add_tree(self.m, rem_word)
        elif self.ch < fch:
            self.l = TernaryTree.add_tree(self.l, word)
        else:
            self.r = TernaryTree.add_tree(self.l, word)

    def search_word(self, word):
        fch = word[0]
        rem_word = word[1:]

        if fch == self.ch:
            if not rem_word and not self.m.ch:
                return True
            return self.m.search_word(rem_word)
        elif fch < self.ch:
            if not self.l:
                return False
            return self.l.search_word(word)
        else:
            if not self.r:
                return False
            return self.r.search_word(word)


# Tests
tt = TernaryTree()
tt.add_word("code")
tt.add_word("cob")
tt.add_word("be")
tt.add_word("ax")
tt.add_word("war")
tt.add_word("we")

assert tt.search_word("code")
assert not tt.search_word("cow")
