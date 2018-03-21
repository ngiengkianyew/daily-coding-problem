def get_positive_subset(array):
    i = 0
    j = len(array) - 1

    while i < j:
        if array[i] > 0 and array[j] <= 0:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
        elif array[i] > 0:
            j -= 1
        else:
            i += 1

    # print("i: {}, j: {}".format(i, j))
    # print("partitioned_array:", array)
    pivot = i if array[i] > 0 else i + 1
    return array[pivot:]


def get_missing_number(array):
    if not array:
        return 1

    array = get_positive_subset(array)
    array_len = len(array)
    # print("array: {}".format(array))

    if not array:
        return 1

    if max(array) == len(array):
        return max(array) + 1

    for num in array:
        current_num = abs(num)
        if (current_num - 1) < array_len:
            array[current_num - 1] *= -1
    # print("mutated_array: {}".format(array))

    for i, num in enumerate(array):
        if num > 0:
            return i + 1


assert get_missing_number([3, 4, -1, 1]) == 2
assert get_missing_number([1, 2, 0]) == 3
assert get_missing_number([1, 2, 5]) == 3
assert get_missing_number([1]) == 2
assert get_missing_number([-1, -2]) == 1
assert get_missing_number([]) == 1
