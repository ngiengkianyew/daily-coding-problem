from copy import deepcopy


class Node:
    def __init__(self, val):
        self.val = val
        self.l, self.r = None, None

    def __repr__(self):
        return "[{}=>(l={}, r={})]".format(self.val, self.l, self.r)


def get_trees(nodes):
    if not nodes:
        return []
    elif len(nodes) == 1:
        return deepcopy(nodes)

    trees = list()
    for ind, root in enumerate(nodes):
        lefts = get_trees(nodes[:ind]) if ind > 0 else list()
        rights = get_trees(nodes[ind + 1:]) if ind < len(nodes) - 1 else list()

        for left in lefts:
            for right in rights:
                root.l = deepcopy(left)
                root.r = deepcopy(right)
                trees.append(deepcopy(root))

    return trees


def create_trees(n):
    nodes = [Node(x) for x in range(n)]
    return get_trees(nodes)


# Tests
trees = create_trees(5)
print(trees)
