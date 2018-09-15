from copy import deepcopy


class Node:
    def __init__(self, id_str):
        self.id = id_str

    def __repr__(self):
        return str(self.id)

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id


class Graph:
    def __init__(self):
        self.nodes = set()
        self.adj_lists = dict()

    def add_edge(self, node_a, node_b):
        for node in [node_a, node_b]:
            if node not in self.nodes:
                self.nodes.add(node)
                self.adj_lists[node] = set()

        self.adj_lists[node_a].add(node_b)
        self.adj_lists[node_b].add(node_a)


def are_connected(g, source, target, seen=set()):
    if source == target:
        return True

    seen_cp = seen.copy()
    seen_cp.add(source)

    return any(are_connected(g, x, target, seen_cp)
               for x in g.adj_lists[source] if x not in seen)


def is_min_graph(g):
    if all(len(x) == 1 for x in g.adj_lists.values()):
        return True

    for node in g.nodes:
        cp_g = deepcopy(g)

        assert node in cp_g.nodes
        adj_nodes = list(cp_g.adj_lists[node])
        cp_g.adj_lists.pop(node)

        for an in adj_nodes:
            cp_g.adj_lists[an].remove(node)

        for i in range(len(adj_nodes)):
            for j in range(i + 1, len(adj_nodes)):
                if are_connected(cp_g, adj_nodes[i], adj_nodes[j]):
                    return False

    return True


# Tests
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

g = Graph()
g.add_edge(a, b)
assert is_min_graph(g)

g.add_edge(b, c)
assert is_min_graph(g)

g.add_edge(a, c)
assert not is_min_graph(g)

g.add_edge(a, d)
assert not is_min_graph(g)
