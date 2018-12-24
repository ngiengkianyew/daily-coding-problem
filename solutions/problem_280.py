class Node:
    def __init__(self, val):
        self.val = val
        self.adj_nodes = set()

    def __hash__(self):
        return hash(self.val)

    def __repr__(self):
        return self.val


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.unseen_nodes = None

    def has_cycle_helper(self, node, path=list()):
        if node in self.unseen_nodes:
            self.unseen_nodes.remove(node)

        for adj_node in node.adj_nodes:
            if adj_node in path and adj_node != path[-1]:
                return True

            if self.unseen_nodes:
                return self.has_cycle_helper(adj_node, path + [node])

        return False

    def has_cycle(self):
        start_node = next(iter(self.nodes))
        self.unseen_nodes = self.nodes.copy()
        return self.has_cycle_helper(start_node)


# Tests
a = Node("a")
b = Node("b")
c = Node("c")

a.adj_nodes = {b}
b.adj_nodes = {c}
c.adj_nodes = {a}

g1 = Graph({a, b, c})
assert g1.has_cycle()

a.adj_nodes = {b, c}
b.adj_nodes = set()
c.adj_nodes = set()
g2 = Graph({a, b, c})
assert not g2.has_cycle()
