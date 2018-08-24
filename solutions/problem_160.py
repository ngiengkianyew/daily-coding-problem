class Node:
    def __init__(self, iden):
        self.iden = iden
        self.max_path = 0
        self.child_dists = list()

    def __repr__(self):
        return "Node(id={},chi={},mp={})".format(
            self.iden, self.child_dists, self.max_path)


def get_path_maxlen(root):
    if not root.child_dists:
        return 0

    path_lens = list()
    child_max_path_lens = list()
    for child, dist in root.child_dists:
        path_lens.append(child.max_path + dist)
        child_max_path_lens.append(get_path_maxlen(child))

    child_max_path_len = max(child_max_path_lens)

    return max(sum(sorted(path_lens)[-2:]), child_max_path_len)


def update_max_paths(root):
    if not root.child_dists:
        root.max_path = 0
        return

    root_paths = list()
    for child, dist in root.child_dists:
        update_max_paths(child)
        root_paths.append(child.max_path + dist)

    root.max_path = max(root_paths)


def get_longest_path(root):
    update_max_paths(root)
    return get_path_maxlen(root)


# Tests
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

e.child_dists = [(g, 1), (h, 1)]
d.child_dists = [(e, 2), (f, 4)]
a.child_dists = [(b, 3), (c, 5), (d, 8)]

assert get_longest_path(a) == 17
