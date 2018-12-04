def deduce_nums(arr):
    ln = len(arr)
    count_gt = sum([1 for x in arr if x == '+'])
    first = ln - count_gt - 1
    nums = [first]
    small, large = first - 1, first + 1
    for sym in arr[1:]:
        if sym == '+':
            nums.append(large)
            large += 1
        else:
            nums.append(small)
            small -= 1
    
    return nums


# Tests
assert deduce_nums([None, '+', '+', '-', '+']) == [1, 2, 3, 0, 4]
