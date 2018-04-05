def get_minimum_painting_cost(cost_matrix, num_houses, num_colors):
    for i in range(1, num_houses):
        for j in range(num_colors):
            # get minimum possible cost of painting the previous
            # house using a different color
            candidates = cost_matrix[i-1][:j]
            if j < num_colors - 1:
                candidates.extend(cost_matrix[i-1][j+1:])

            # and add it to the current cost of painting
            cost_matrix[i][j] += min(candidates)

    # return the minimal cumulative cost on the last house
    return min(cost_matrix[-1])


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
