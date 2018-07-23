def swap_indices(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def pull_elements_to_front(arr, start_index, end_index, letter):
    i = start_index
    j = end_index
    last_letter_index = -1

    while i < j:
        if arr[i] == letter:
            last_letter_index = i
            i += 1
        elif arr[j] != letter:
            j -= 1
        else:
            last_letter_index = i
            swap_indices(arr, i, j)

    return last_letter_index


def reorder_array(arr):
    last_index = pull_elements_to_front(arr, 0, len(arr) - 1, "R")
    pull_elements_to_front(arr, last_index + 1, len(arr) - 1, "G")

    return arr


assert reorder_array(['G', 'R']) == ['R', 'G']
assert reorder_array(['G', 'B', 'R']) == ['R', 'G', 'B']
assert reorder_array(['B', 'G', 'R']) == ['R', 'G', 'B']
assert reorder_array(['G', 'B', 'R', 'R', 'B', 'R', 'G']) == [
    'R', 'R', 'R', 'G', 'G', 'B', 'B']
