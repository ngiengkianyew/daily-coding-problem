class BitArray:
    def __init__(self, size):
        self.set_indices = set()
        self.size = size

    def get_list_rep(self):
        arr = list()
        for i in range(self.size):
            if i in self.set_indices:
                arr.append(1)
            else:
                arr.append(0)
        return arr

    def set_val(self, i, val):
        if i >= self.size:
            raise LookupError("Invalid Index")

        if val and i not in self.set_indices:
            self.set_indices.add(i)
        elif not val and i in self.set_indices:
            self.set_indices.remove(i)

    def get_val(self, i):
        if i >= self.size:
            raise LookupError("Invalid Index")
        return int(i in self.set_indices)


# Tests
ba = BitArray(10)
assert ba.get_list_rep() == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ba.set_val(3, 1)
assert ba.get_list_rep() == [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
ba.set_val(6, 1)
ba.set_val(8, 1)
ba.set_val(3, 0)
assert ba.get_list_rep() == [0, 0, 0, 0, 0, 0, 1, 0, 1, 0]


# Exceptions
try:
    ba.set_val(10, 1)
except LookupError as le:
    print(le)
try:
    ba.get_val(10)
except LookupError as le:
    print(le)
