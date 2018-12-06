from queue import Queue


class Node:
    def __init__(self, char, count):
        self.ch = char
        self.ct = count
        self.lt = None
        self.rt = None

    def __repr__(self):
        return "{}=>[ct={},lt={},rt={}]".format(self.ch, self.ct, self.lt, self.rt)


def parse_queue_and_get_tree(nq):
    if nq.qsize() == 1:
        node = nq.get()
        return node

    n1 = nq.get()
    n2 = nq.get()

    par = Node(None, n1.ct + n2.ct)
    par.lt = n1
    par.rt = n2

    nq.put(par)

    return parse_queue_and_get_tree(nq)


def build_tree(words):
    ch_dict = dict()
    for word in words:
        for char in word:
            if not char in ch_dict:
                ch_dict[char] = 0
            ch_dict[char] += 1
    print(ch_dict)

    nodes = list()
    for char in ch_dict:
        nodes.append(Node(char, ch_dict[char]))
    nodes.sort(key=lambda x: x.ct)
    if not nodes:
        return Node(None, 0)

    nq = Queue()
    for node in nodes:
        nq.put(node)

    tree = parse_queue_and_get_tree(nq)
    return tree


def update_char_map(htree, char_map, hcode=""):
    if htree.ch:
        char_map[htree.ch] = hcode
        return

    update_char_map(htree.lt, char_map, hcode + "0")
    update_char_map(htree.rt, char_map, hcode + "1")


# Tests
htree = build_tree(["cats", "cars", "dogs"])
char_map = dict()
update_char_map(htree, char_map)
print(char_map)

htree = build_tree(["cat", "car", "dog"])
char_map = dict()
update_char_map(htree, char_map)
print(char_map)
