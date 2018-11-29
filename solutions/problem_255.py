def update_transitive_closure(orig, node, adjacency_list, transitive_closure):
    if len(adjacency_list[node]) == 1:
        return

    for adj_node in adjacency_list[node]:
        if orig == adj_node or node == adj_node:
            continue
        transitive_closure[orig][adj_node] = 1
        update_transitive_closure(
            orig, adj_node, adjacency_list, transitive_closure)


def get_transitive_closure(adjacency_list):
    transitive_closure = \
        [[0 for _ in range(len(adjacency_list))]
         for _ in range(len(adjacency_list))]
    for i in range(len(adjacency_list)):
        transitive_closure[i][i] = 1

    for i in adjacency_list:
        update_transitive_closure(i, i, adjacency_list, transitive_closure)

    return transitive_closure


# Tests
adjacency_list = {
    0: [0, 1, 3],
    1: [1, 2],
    2: [2],
    3: [3]
}
assert get_transitive_closure(adjacency_list) == \
    [[1, 1, 1, 1],
     [0, 1, 1, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 1]]
