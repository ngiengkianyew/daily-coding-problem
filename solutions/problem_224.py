def findSmallest(arr):
    res = 1
    for num in arr:
        if num > res:
            break
        res += num
    return res


# Tests
assert findSmallest([1, 2, 3, 10]) == 7
assert findSmallest([1, 2, 10]) == 4
assert findSmallest([0, 10]) == 1
