import itertools


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "[Cell(x={},y={})]".format(self.x, self.y)


def get_adj_options(matrix, size, row, col, seen):
    adj_options = list()
    if row > 0:
        adj_options.append(Cell(row - 1, col))
    if row < size - 1:
        adj_options.append(Cell(row + 1, col))
    if col > 0:
        adj_options.append(Cell(row, col - 1))
    if col < size - 1:
        adj_options.append(Cell(row, col + 1))

    adj_options = [x for x in adj_options if x not in seen]
    return adj_options


def consume_word(start, word, matrix, size, seen_cells):
    # print("Consuming. start:{}, word:{}, seen:{}".format(start, word, seen_cells))
    if not word:
        return [(True, seen_cells)]
    if matrix[start.x][start.y] != word[0]:
        return [(False, set())]

    seen = seen_cells | {start}
    adj_cells = get_adj_options(matrix, size, start.x, start.y, seen)

    results = list()
    for adj_cell in adj_cells:
        result = consume_word(adj_cell, word[1:], matrix, size, seen)
        results.extend(result)

    return results


def get_max_packed(matrix, dictionary, size, seen, packed):
    cell_occ = dict()
    for word in dictionary:
        cell_occ[word] = list()
        for i in range(size):
            for k in range(size):
                possibilities = consume_word(
                    Cell(i, k), word, matrix, size, set())
                consumed = [y for (x, y) in possibilities if x]
                if consumed:
                    cell_occ[word].extend(consumed)

    max_perm_length = len(dictionary)
    while max_perm_length > 0:
        all_seen = set()
        perms = itertools.combinations(dictionary, max_perm_length)
        for perm in perms:
            count_words = 0
            for word in perm:
                independent, val = False, None
                for poss in cell_occ[word]:
                    if poss & all_seen:
                        continue
                    independent, val = True, poss
                if independent:
                    all_seen |= val
                    count_words += 1
            if count_words == max_perm_length:
                return max_perm_length

        max_perm_length -= 1

    return 1


def get_max_packed_helper(matrix, dictionary):
    print(get_max_packed(matrix, dictionary, len(matrix), set(), set()))


# Tests
matrix = \
    [
        ['e', 'a', 'n'],
        ['t', 't', 'i'],
        ['a', 'r', 'a']
    ]
dictionary = {'eat', 'rain', 'in', 'rat'}
get_max_packed_helper(matrix, dictionary)
