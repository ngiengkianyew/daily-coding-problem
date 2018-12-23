import random


def populate_group(node, adj_list, group):
    group.add(node)

    adj_nodes = adj_list[node]
    if not adj_nodes:
        return

    for anode in adj_nodes:
        if anode not in group:
            populate_group(anode, adj_list, group)


def get_groups(nodes, adj_list, groups):
    num_nodes = len(nodes)
    while num_nodes:
        new_group = set()
        node = list(nodes)[0]
        populate_group(node, adj_list, new_group)
        groups.append(new_group)
        nodes -= new_group
        num_nodes = len(nodes)

    return groups


def get_num_groups(nodes, adj_list):
    groups = list()
    isolated = set()
    for node in nodes:
        if not adj_list[node]:
            isolated.add(node)

    for node in isolated:
        groups.append({node})
        nodes.remove(node)
        del adj_list[node]

    groups = get_groups(nodes, adj_list, groups)
    print(groups)
    return len(groups)


# Tests
adj_list = {
    0: [1, 2],
    1: [0, 5],
    2: [0],
    3: [6],
    4: [],
    5: [1],
    6: [3]
}
assert get_num_groups(set(range(7)), adj_list) == 3
