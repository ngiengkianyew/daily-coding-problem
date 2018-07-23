import sys


def get_minimum_painting_cost(cost_matrix, num_houses, num_colors):
    if not cost_matrix:
        return 0

    prev_house_min = 0
    prev_house_min_index = -1
    prev_house_second_min = 0

    for i in range(num_houses):
        curr_house_min = sys.maxsize
        curr_house_second_min = sys.maxsize
        curr_house_min_index = 0

        for j in range(num_colors):
            if prev_house_min_index == j:
                cost_matrix[i][j] += prev_house_second_min
            else:
                cost_matrix[i][j] += prev_house_min

            if curr_house_min > cost_matrix[i][j]:
                curr_house_second_min = curr_house_min
                curr_house_min = cost_matrix[i][j]
                curr_house_min_index = j
            elif curr_house_second_min > cost_matrix[i][j]:
                curr_house_second_min = cost_matrix[i][j]

        prev_house_min = curr_house_min
        prev_house_second_min = curr_house_second_min
        prev_house_min_index = curr_house_min_index

    return min(cost_matrix[num_houses - 1])


cost_matrix = \
    [[7, 3, 8, 6, 1, 2],
     [5, 6, 7, 2, 4, 3],
     [10, 1, 4, 9, 7, 6]]
assert get_minimum_painting_cost(cost_matrix,
                                 len(cost_matrix), len(cost_matrix[0])) == 4

cost_matrix = \
    [[7, 3, 8, 6, 1, 2],
     [5, 6, 7, 2, 4, 3],
     [10, 1, 4, 9, 7, 6],
     [10, 1, 4, 9, 7, 6]]
assert get_minimum_painting_cost(cost_matrix,
                                 len(cost_matrix), len(cost_matrix[0])) == 8
