def get_smaller_right(arr):
    smaller_right_arr = list()
    for i in range(len(arr)):
        smaller_count = 0
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                smaller_count += 1
        smaller_right_arr.append(smaller_count)

    return smaller_right_arr


# Tests

assert get_smaller_right([3, 4, 9, 6, 1]) == [1, 1, 2, 1, 0]
