class SubarraySumOptimizer:
    def __init__(self, arr):
        self.arr = arr
        total = 0
        self.larr = [total]
        for num in self.arr:
            total += num
            self.larr.append(total)

    def sum(self, start, end):
        if start < 0 or end > len(self.arr) or start > end:
            return 0
        return self.larr[end] - self.larr[start]


# Tests
sso = SubarraySumOptimizer([1, 2, 3, 4, 5])
assert sso.sum(1, 3) == 5
assert sso.sum(0, 5) == 15
assert sso.sum(0, 4) == 10
assert sso.sum(3, 4) == 4
assert sso.sum(3, 3) == 0
