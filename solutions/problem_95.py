def get_greater_permutation(arr):

    if len(arr) < 2:
        return

    for index in range(len(arr) - 1, -1, -1):
        if index > 0 and arr[index - 1] < arr[index]:
            break

    if index == 0:
        arr.reverse()
    else:
        for k in range(len(arr) - 1, index - 1, -1):
            if arr[k] > arr[index - 1]:
                tmp = arr[k]
                arr[k] = arr[index - 1]
                arr[index - 1] = tmp
                break

        sub_array = arr[index:]
        sub_array.reverse()
        arr[index:] = sub_array

    return arr


assert get_greater_permutation([1, 2, 3]) == [1, 3, 2]
assert get_greater_permutation([1, 3, 2]) == [2, 1, 3]
assert get_greater_permutation([3, 2, 1]) == [1, 2, 3]
