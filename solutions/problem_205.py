from bisect import bisect


def get_next_perm(num):
    num_str = str(num)

    # if the number is already maxed out, return it
    max_val_str = "".join(sorted(num_str, reverse=True))
    if max_val_str == num_str:
        return num

    # find the point n the number at which there is
    # a chance to increase the number by changing order
    right_nums = list()
    num_to_replace = None
    for i in range(len(num_str) - 2, -1, -1):
        right_nums.append(num_str[i + 1])
        if num_str[i] < num_str[i + 1]:
            num_to_replace = num_str[i]
            break

    # identify the replacement of the digit to be moved
    rep_index = bisect(right_nums, num_to_replace)
    replacement = right_nums[rep_index]

    # replace digit
    right_nums[rep_index] = num_to_replace
    leftover_nums = num_str[:i]

    # contruct new number
    final_str = "{}{}{}".format(leftover_nums, replacement,
                                "".join(sorted(right_nums)))

    return int(final_str)


# Tests
assert get_next_perm(98754) == 98754
assert get_next_perm(48975) == 49578
assert get_next_perm(48759) == 48795
assert get_next_perm(49875) == 54789
assert get_next_perm(408975) == 409578
