def merge_sorted(arr_1, arr_2):
    merged_array = list()
    ind_1, ind_2 = 0, 0
    while ind_1 < len(arr_1) and ind_2 < len(arr_2):
        if arr_1[ind_1] <= arr_2[ind_2]:
            merged_array.append(arr_1[ind_1])
            ind_1 += 1
        else:
            merged_array.append(arr_2[ind_2])
            ind_2 += 1

    while ind_1 < len(arr_1):
        merged_array.append(arr_1[ind_1])
        ind_1 += 1
    while ind_2 < len(arr_2):
        merged_array.append(arr_2[ind_2])
        ind_2 += 1

    return merged_array


def reverse(lst, i, j):
    return list(reversed(lst[i:j+1]))


def custom_sort(lst):
    # create segments of sorted sub-arrays
    start, end = None, None
    last_end = -1
    sorted_segments = list()
    for i in range(1, len(lst)):
        if lst[i] < lst[i-1]:
            if not start:
                segment = lst[last_end+1: i-1]
                if segment:
                    sorted_segments.append(segment)
                start = i - 1
        elif start:
            end = i - 1
            if end > start:
                sorted_segments.append(reverse(lst, start, end))
                last_end = end
                start, end = None, None
    if start:
        end = len(lst) - 1
        if end > start:
            sorted_segments.append(reverse(lst, start, end))
    else:
        segment = lst[last_end+1:]
        if segment:
            sorted_segments.append(segment)

    # merge the sorted sub-arrays
    final_sorted = list()
    for segment in sorted_segments:
        final_sorted = merge_sorted(final_sorted, segment)

    return final_sorted


# Tests
assert custom_sort([0, 6, 4, 2, 5, 3, 1]) == [
    0, 1, 2, 3, 4, 5, 6]
assert custom_sort([0, 6, 4, 2, 5, 3, 1, 10, 9]) == [
    0, 1, 2, 3, 4, 5, 6, 9, 10]
assert custom_sort([0, 6, 4, 2, 5, 3, 1, 2, 3]) == [
    0, 1, 2, 2, 3, 3, 4, 5, 6]
assert custom_sort([0, 6, 4, 2, 5, 3, 1, 11]) == [
    0, 1, 2, 3, 4, 5, 6, 11]
