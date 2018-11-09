def find_min_max(nums):
    mini = maxi = nums[0]
    for num in nums[1:]:
        if num < mini:
            mini = num
            continue
        elif num > maxi:
            maxi = num

    return mini, maxi


# Tests
assert find_min_max([4, 3, 1, 2, 5]) == (1, 5)
