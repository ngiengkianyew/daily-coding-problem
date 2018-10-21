class Node:
    def __init__(self, iden):
        self.iden = iden

    def __hash__(self):
        return hash(self.iden)

    def __eq__(self, other):
        return self.iden == other.iden

    def __repr__(self):
        return str(self.iden)


class Edge:
    def __init__(self, src, tgt):
        self.src = src
        self.tgt = tgt

    def __hash__(self):
        return hash((self.src, self.tgt))

    def __eq__(self, other):
        return self.src == other.src and self.tgt == other.tgt

    def __repr__(self):
        return "{}->{}".format(self.src, self.tgt)

    def reverse(self):
        tmp_node = self.src
        self.src = self.tgt
        self.tgt = tmp_node


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = set()

    def add_node(self, node):
        if node in self.nodes:
            return
        self.nodes.add(node)

    def add_edge(self, src_node, tgt_node):
        self.edges.add(Edge(src_node, tgt_node))

    def reverse_edges(self):
        self.edges = [Edge(x.tgt, x.src) for x in self.edges]

    def get_edges(self):
        return self.edges


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
edges = g.get_edges()
assert Edge(a, b) in edges and Edge(b, c) in edges and len(edges) == 2

g.reverse_edges()
edges = g.get_edges()
assert Edge(b, a) in edges and Edge(c, b) in edges and len(edges) == 2
