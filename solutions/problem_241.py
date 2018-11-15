def get_h_index(citations):
    citations.sort(reverse=True)

    for i, cit_count in enumerate(citations):
        if i >= cit_count:
            return i


# Tests
assert get_h_index([4, 3, 0, 1, 5]) == 3
assert get_h_index([4, 1, 0, 1, 1]) == 1
assert get_h_index([4, 4, 4, 5, 4]) == 4
