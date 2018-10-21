class Node:
    def __init__(self, iden):
        self.iden = iden

    def __hash__(self):
        return hash(self.iden)

    def __eq__(self, other):
        return self.iden == other.iden

    def __repr__(self):
        return str(self.iden)


class Graph:
    def __init__(self):
        self.nodes = dict()
        self.adjacency_matrix = None

    def add_node(self, node):
        if node in self.nodes:
            return
        self.nodes[node] = len(self.nodes)

        if not self.adjacency_matrix:
            self.adjacency_matrix = [[0]]
        else:
            for i in range(len(self.nodes) - 1):
                self.adjacency_matrix[i] += [0]
            self.adjacency_matrix.append([0] * len(self.nodes))

    def add_edge(self, src_node, tgt_node):
        self.adjacency_matrix[self.nodes[src_node]][self.nodes[tgt_node]] = 1

    def reverse_edges(self):
        new_adj_matrix = [[0 for node in self.nodes] for node in self.nodes]

        for i, row in enumerate(self.adjacency_matrix):
            for k, _ in enumerate(row):
                if self.adjacency_matrix[i][k]:
                    new_adj_matrix[k][i] = 1

        self.adjacency_matrix = new_adj_matrix

    def get_edges(self):
        edges = set()
        node_index = {num: node for node, num in self.nodes.items()}
        for i, row in enumerate(self.adjacency_matrix):
            for k, _ in enumerate(row):
                if self.adjacency_matrix[i][k]:
                    edges.add("{}->{}".format(node_index[i], node_index[k]))
        return edges


# Tests
g = Graph()
a = Node('a')
b = Node('b')
c = Node('c')

g.add_node(a)
g.add_node(b)
g.add_node(c)
g.add_edge(a, b)
g.add_edge(b, c)
assert g.get_edges() == {'b->c', 'a->b'}

g.reverse_edges()
assert g.get_edges() == {'c->b', 'b->a'}
