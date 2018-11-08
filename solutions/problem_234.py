class Node:
    def __init__(self, val):
        self.val = val

    def __hash__(self):
        return hash(self.val)

    def __repr__(self):
        return str(self.val)


class Edge:
    def __init__(self, target, weight):
        self.target = target
        self.weight = weight

    def __hash__(self):
        return hash(self.target)

    def __repr__(self):
        return "-{}-> {}".format(self.weight, self.target)


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = dict()

    def add_node(self, node):
        self.nodes.add(node)
        self.edges[node] = set()

    def add_edge(self, source, target, weight):
        if source not in self.nodes:
            self.add_node(source)
        if target not in self.nodes:
            self.add_node(target)

        self.edges[source].add(Edge(target, weight))
        self.edges[target].add(Edge(source, weight))


def get_max_span_helper(g, start, remaining, score):
    if not remaining:
        return score

    scores = list()
    for edge in g.edges[start]:
        if edge.target in remaining:
            rem_cp = remaining.copy()
            rem_cp.remove(edge.target)
            new_score = get_max_span_helper(
                g, edge.target, rem_cp, score + edge.weight)
            scores.append(new_score)

    return max(scores)


def get_max_span(g):
    remaining = g.nodes.copy()
    start_node = list(remaining)[0]
    remaining.remove(start_node)

    score = get_max_span_helper(g, start_node, remaining, 0)
    return score


# Tests
g = Graph()
a = Node('a')
b = Node('b')
c = Node('c')
g.add_edge(a, b, 1)
g.add_edge(a, c, 2)
g.add_edge(b, c, 3)


assert get_max_span(g) == 5
