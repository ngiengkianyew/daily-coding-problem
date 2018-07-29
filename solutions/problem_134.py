class SparseArray:

    def __init__(self):
        self.storage = dict()

    def __repr__(self):
        return str(self.storage)

    def init(self, arr, size):
        for i, num in enumerate(arr):
            if num:
                self.storage[i] = num

    def set_val(self, i, val):
        if not val:
            del self.storage[i]
        else:
            self.storage[i] = val

    def get_val(self, i):
        if i not in self.storage:
            return None

        return self.storage[i]


# Tests

arr = [1, 0, 0, 0, 3, 0, 2]

sa = SparseArray()
sa.init(arr, len(arr))
assert sa.storage == {0: 1, 4: 3, 6: 2}

sa.set_val(2, 4)
assert sa.get_val(2) == 4
sa.set_val(4, 1)
assert sa.get_val(4) == 1
sa.set_val(0, 0)
assert not sa.get_val(0)
