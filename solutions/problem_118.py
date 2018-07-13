def merge_sorted_lists(arr1, arr2):
    i, k = 0, 0
    merged = list()
    while i < len(arr1) and k < len(arr2):
        if arr1[i] <= arr2[k]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[k])
            k += 1

    merged += arr1[i:]
    merged += arr2[k:]

    return merged


def sort_squares(arr):
    first_pos_index = 0
    for num in arr:
        if num >= 0:
            break
        first_pos_index += 1

    neg_nums = [x ** 2 for x in reversed(arr[:first_pos_index])]
    pos_nums = [x ** 2 for x in arr[first_pos_index:]]

    return merge_sorted_lists(pos_nums, neg_nums)


assert sort_squares([]) == []
assert sort_squares([0]) == [0]
assert sort_squares([-1, 1]) == [1, 1]
assert sort_squares([0, 2, 3]) == [0, 4, 9]
assert sort_squares([-9, -2, 0]) == [0, 4, 81]
assert sort_squares([-9, -2, 0, 2, 3]) == [0, 4, 4, 9, 81]
