from typing import Set, Dict

DAMPING = 0.85


class Graph:
    def __init__(self):
        self.edges = dict()

    def __repr__(self):
        return str(self.edges)

    def add_edge(self, src, tgt):
        if not src in self.edges:
            self.edges[src] = set()
        if not tgt in self.edges:
            self.edges[tgt] = set()

        self.edges[src].add(tgt)


def calculate_score(node: str, g: Graph, page_scores: Dict):
    agg_score = 0
    for other in g.edges:
        if node in g.edges[other]:
            agg_score += page_scores[other] / len(g.edges[other])

    score = ((1 - DAMPING) / len(g.edges)) + (DAMPING * agg_score)
    return score


def rank_pages(g: Graph):
    page_scores = dict()
    start_prob = 1 / len(g.edges)
    for node in g.edges.keys():
        page_scores[node] = start_prob

    for node in g.edges.keys():
        page_scores[node] = calculate_score(node, g, page_scores)

    return page_scores


# Tests
g = Graph()
g.add_edge('a', 'b')
g.add_edge('a', 'c')
g.add_edge('b', 'c')
print(rank_pages(g))
