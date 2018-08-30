class TwoDimIterator:

    def __init__(self, arrays):
        self.arrays = arrays
        self.gen = self.get_generator()
        self.next_val = next(self.gen)

    def get_generator(self):
        for array in self.arrays:
            for num in array:
                yield num

    def has_next(self):
        return self.next_val != None

    def next(self):
        val = self.next_val
        try:
            self.next_val = next(self.gen)
        except StopIteration:
            self.next_val = None

        return val


# Tests

tdi = TwoDimIterator([[0, 1, 2], [3], [], [4, 5, 6]])

assert tdi.has_next()
assert tdi.next() == 0
assert tdi.next() == 1
assert tdi.next() == 2
assert tdi.has_next()
assert tdi.next() == 3
assert tdi.next() == 4
assert tdi.next() == 5
assert tdi.has_next()
assert tdi.next() == 6
assert not tdi.has_next()
assert not tdi.next()
