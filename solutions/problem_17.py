class Node:
    def __init__(self, name, pathtype):
        self.name = name
        self.type = pathtype
        self.children = list()
        self.length = len(name)
        self.max_child_length = 0

    def __repr__(self):
        return "(name={}, type={}, len={}, max_child_len={})".format(
            self.name, self.type, self.length, self.max_child_length)


def create_graph(node_list):
    if not node_list:
        return None

    parent_node = node_list[0][1]
    level = node_list[0][0]

    for index, (node_level, _) in enumerate(node_list[1:]):
        if node_level <= level:
            break
        if node_level == level + 1:
            child_node = create_graph(node_list[index + 1:])
            parent_node.children.append(child_node)
            if child_node.children or child_node.type == 'file':
                if child_node.max_child_length + child_node.length > parent_node.max_child_length:
                    parent_node.max_child_length = child_node.max_child_length + child_node.length

    # print("current_parent: {}".format(parent_node))
    # print("it's children: {}".format(parent_node.children))

    return parent_node


def get_path_type(name):
    return 'file' if '.' in name else 'directory'


def get_longest_path(s):
    if not s:
        return 0

    individual_lines = s.split('\n')
    split_lines = [x.split('\t') for x in individual_lines]
    annotated_lines = [
        (len(x) - 1, Node(name=x[-1], pathtype=get_path_type(x[-1])))
        for x in split_lines]

    graph = create_graph(annotated_lines)

    return graph.max_child_length + graph.length if graph.max_child_length > 0 else 0


assert get_longest_path("dir\n\tsubdir1\n\tsubdir2") == 0
assert get_longest_path("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext") == 18
assert get_longest_path(
    "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\t" +
    "subsubdir2\n\t\t\tfile2.ext") == 29
