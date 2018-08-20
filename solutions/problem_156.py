import math


def get_candidate_squares(num):
    candidates = list()
    for candidate_root in range(1, int(num/2)):
        candidate = candidate_root * candidate_root
        if candidate > num:
            break
        candidates.append(candidate)
    candidates.reverse()
    return candidates


def get_min_squares_helper(num, candidates):
    candidate_square = candidates[0]
    max_used = int(num / candidate_square)
    remaining = num % candidate_square

    if remaining == 0:
        return max_used

    return max_used + get_min_squares_helper(remaining, candidates[1:])


def get_min_squares(num):
    candidates = get_candidate_squares(num)
    return get_min_squares_helper(num, candidates)


# Tests
assert get_min_squares(13) == 2
assert get_min_squares(25) == 1
assert get_min_squares(27) == 3
