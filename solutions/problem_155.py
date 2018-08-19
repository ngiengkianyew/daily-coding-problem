import math


def get_majority_element(arr):
    threshold = math.floor(len(arr) / 2)
    occurrences = dict()
    for num in arr:
        if num not in occurrences:
            occurrences[num] = 0
        occurrences[num] += 1
    for num in occurrences:
        if occurrences[num] > threshold:
            return num



# Tests
assert get_majority_element([]) == None
assert get_majority_element([0]) == 0
assert get_majority_element([0, 2, 2]) == 2
assert get_majority_element([1, 2, 1, 1, 3, 4, 1]) == 1
