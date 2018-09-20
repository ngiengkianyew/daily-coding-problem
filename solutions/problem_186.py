def get_diff(s1, s1_sum, s2, s2_sum, score):
    min_diff, min_cand = score, None
    for i, num in enumerate(s1):
        new_s1_sum, new_s2_sum = s1_sum - num, s2_sum + num
        new_score = abs(new_s1_sum - new_s2_sum)
        if new_score < min_diff:
            min_diff = new_score
            min_cand = (s1[:i] + s1[i + 1:], new_s1_sum,
                        s2 + [num], new_s2_sum)

    if not min_cand:
        return (set(s1), set(s2))

    return get_diff(min_cand[0], min_cand[1], min_cand[2], min_cand[3], min_diff)


def divide_numbers(nums):
    sum_nums = sum(nums)
    best_sets = get_diff(nums.copy(), sum_nums, [], 0, sum_nums)

    return best_sets


# Tests
assert divide_numbers([5, 10, 15, 20, 25]) == ({5, 15, 20}, {10, 25})
assert divide_numbers([5, 10, 15, 20]) == ({10, 15}, {20, 5})
