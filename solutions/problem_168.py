def rotate_matrix(m):
    num_layers = len(m) // 2
    max_ind = len(m) - 1

    for layer in range(num_layers):
        # rotate all numbers
        for ind in range(layer, max_ind - layer):
            # rotate 4 numbers
            temp = m[layer][ind]
            m[layer][ind] = m[max_ind - ind][layer]
            m[max_ind - ind][layer] = m[max_ind - layer][max_ind - ind]
            m[max_ind - layer][max_ind - ind] = m[ind][max_ind - layer]
            m[ind][max_ind - layer] = temp


# Tests
matrix_1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
rotate_matrix(matrix_1)
assert matrix_1 == [[7, 4, 1],
                    [8, 5, 2],
                    [9, 6, 3]]

matrix_2 = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]
rotate_matrix(matrix_2)
assert matrix_2 == [[13, 9, 5, 1],
                    [14, 10, 6, 2],
                    [15, 11, 7, 3],
                    [16, 12, 8, 4]]
