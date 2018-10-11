class Node:
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return str(self.val)


class Graph:
    def __init__(self):
        self.nodes, self.edges = set(), dict()
        self.set_1, self.set_2 = set(), set()

    def is_bipartite(self):
        sorted_nodes = sorted(self.edges.items(),
                              key=lambda x: len(x[1]), reverse=True)
        for node, _ in sorted_nodes:
            if node in self.set_2:
                continue
            self.set_1.add(node)

            if self.edges[node]:
                for other_node in self.edges[node]:
                    self.set_2.add(other_node)

        for node in self.set_2:
            if self.edges[node]:
                for other_node in self.edges[node]:
                    if other_node in self.set_2:
                        return False

        return True


# Tests
g = Graph()
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g.nodes = set([a, b, c, d, e, f])

g.edges[a] = set([d])
g.edges[b] = set([d, e, f])
g.edges[c] = set([f])
g.edges[d] = set([a, b])
g.edges[e] = set([b])
g.edges[f] = set([b, c])
assert g.is_bipartite()

g.edges = dict()
g.nodes = set([a, b, c, d, e, f])
g.edges[a] = set([d])
g.edges[b] = set([d, e, f])
g.edges[c] = set([f])
g.edges[d] = set([a, b])
g.edges[e] = set([b, f])
g.edges[f] = set([b, c, e])
assert not g.is_bipartite()
