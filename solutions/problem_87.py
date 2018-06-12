opposites = {
    'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'
}


class Node:
    def __init__(self, val):
        self.val = val
        self.neighbours = {
            'N': set(),
            'S': set(),
            'E': set(),
            'W': set()
        }

    def __repr__(self):
        string = "{}={}".format(self.val, self.neighbours)
        return string

    def __hash__(self):
        return hash(self.val)


class Map:

    def add_rule(self, node_1, direction, node_2):

        for char in direction:
            if node_1 in node_2.neighbours[char] or \
                    node_2 in node_1.neighbours[opposites[char]]:
                raise Exception

            for node in node_1.neighbours[char]:
                self.add_rule(node, char, node_2)

        for char in direction:
            node_2.neighbours[char].add(node_1)
            node_1.neighbours[opposites[char]].add(node_2)


a = Node('a')
b = Node('b')
c = Node('c')

m = Map()
m.add_rule(a, 'N', b)
m.add_rule(b, 'NE', c)
try:
    m.add_rule(c, 'N', a)
except Exception:
    print("Invalid rule")
