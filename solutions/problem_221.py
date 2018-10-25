def get_nth_sevenish(n):
    if n < 1:
        raise Exception("Invalid value for 'n'")

    power = 0
    sevenish_nums = list()
    while len(sevenish_nums) < n:
        num = 7 ** power
        new_sevenish_nums = [num]
        for old in sevenish_nums:
            if len(sevenish_nums) + len(new_sevenish_nums) == n:
                return new_sevenish_nums[-1]
            new_sevenish_nums.append(num + old)

        sevenish_nums += new_sevenish_nums
        power += 1

    return sevenish_nums[-1]


# Tests
assert get_nth_sevenish(1) == 1
assert get_nth_sevenish(2) == 7
assert get_nth_sevenish(3) == 8
assert get_nth_sevenish(10) == 350
