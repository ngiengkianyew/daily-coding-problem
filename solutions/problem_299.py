def connect_houses(pipe_costs, houses, total_cost):
    if not houses:
        return total_cost

    costs = list()
    for start_node in (pipe_costs.keys() - houses):
        for adj_node in (pipe_costs[start_node].keys() & houses):
            cost = connect_houses(pipe_costs, houses - {adj_node},
                                  total_cost + pipe_costs[start_node][adj_node])
            costs.append(cost)

    return min(costs)


def get_min_cost(pipe_costs):
    houses = pipe_costs.keys() - {'plant'}
    return connect_houses(pipe_costs, houses, 0)


# Tests
pipe_costs = {
    'plant': {'A': 1, 'B': 5, 'C': 20},
    'A': {'C': 15},
    'B': {'C': 10},
    'C': {}
}
assert get_min_cost(pipe_costs) == 16
