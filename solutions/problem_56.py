def can_color_graph(adjacency_matrix, k):
    max_adjacencies = 0
    for row in adjacency_matrix:
        max_adjacencies = max(max_adjacencies, sum(row))

    return k > max_adjacencies


adjacency_matrix_1 = [
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 0],
]
assert can_color_graph(adjacency_matrix_1, 4)
assert not can_color_graph(adjacency_matrix_1, 3)

adjacency_matrix_2 = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]
assert can_color_graph(adjacency_matrix_2, 4)
assert can_color_graph(adjacency_matrix_2, 1)

adjacency_matrix_3 = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0],
]
assert can_color_graph(adjacency_matrix_3, 4)
assert can_color_graph(adjacency_matrix_3, 3)
assert not can_color_graph(adjacency_matrix_3, 2)
