def find_distance(target, edge_dict):
    if target == 0:
        return 0

    cand_target_distances = edge_dict[target]
    distances = list()
    for cand_tgt, cand_dist in cand_target_distances:
        dist = cand_dist + find_distance(cand_tgt, edge_dict)
        distances.append(dist)

    return min(distances)


def get_shortest_trip(edges, node_count):
    edge_dict = dict()
    for edge in edges:
        start, end, dist = edge
        if end not in edge_dict:
            edge_dict[end] = list()
        edge_dict[end].append((start, dist))

    distances = list()
    for target in set(range(1, node_count + 1)):
        dist = find_distance(target, edge_dict)
        distances.append(dist)

    return max(distances)


# Tests
edges = [
    (0, 1, 5),
    (0, 2, 3),
    (0, 5, 4),
    (1, 3, 8),
    (2, 3, 1),
    (3, 5, 10),
    (3, 4, 5)
]
assert get_shortest_trip(edges, 5) == 9
