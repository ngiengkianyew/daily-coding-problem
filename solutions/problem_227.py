NUM_ROWS, NUM_COLS = 4, 4
WORD_END_CHAR = '0'


class Trie:
    def __init__(self):
        self.size = 0
        self.letter_map = dict()

    def __repr__(self):
        return str(self.letter_map)

    def add_word(self, word):
        if not word:
            self.letter_map[WORD_END_CHAR] = None
            return
        letter = word[0]

        sub_trie = None
        if letter in self.letter_map:
            sub_trie = self.letter_map[letter]
        else:
            sub_trie = Trie()
            self.letter_map[letter] = sub_trie

        self.size += 1
        sub_trie.add_word(word[1:])


class Coordinate():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __ne__(self, other):
        return not(self == other)

    def __repr__(self):
        return "C(x={};y={})".format(self.x, self.y)


def get_adjacent_coords(x, y):
    adj_coords = set()

    red_x, red_y = max(0, x - 1), max(0, y - 1)
    inc_x, inc_y = min(NUM_ROWS - 1, x + 1), min(NUM_COLS - 1, y + 1)

    adj_coords.add(Coordinate(x, red_y))
    adj_coords.add(Coordinate(x, inc_y))
    adj_coords.add(Coordinate(red_x, y))
    adj_coords.add(Coordinate(red_x, red_y))
    adj_coords.add(Coordinate(red_x, inc_y))
    adj_coords.add(Coordinate(inc_x, y))
    adj_coords.add(Coordinate(inc_x, red_y))
    adj_coords.add(Coordinate(inc_x, inc_y))

    return adj_coords


def search_for_words(coord, dtrie, seen, board, sol_words, current):
    letter = board[coord.x][coord.y]
    if letter not in dtrie.letter_map:
        # no possibility of creating a word
        return

    current += letter
    next_trie = dtrie.letter_map[letter]
    if WORD_END_CHAR in next_trie.letter_map:
        # a word can end here
        sol_words.add(current)
        # shouldn't return because a valid word
        # might be extended

    adj_coords = get_adjacent_coords(coord.x, coord.y)
    for adj_coord in adj_coords:
        if adj_coord in seen:
            continue

        seen_cp = seen.copy()
        seen_cp.add(adj_coord)
        search_for_words(adj_coord, next_trie, seen_cp,
                         board, sol_words, current)


def solve_boggle(board, dictionary):
    assert len(board) == NUM_ROWS
    assert len(board[0]) == NUM_COLS

    dtrie = Trie()
    for word in dictionary:
        dtrie.add_word(word)

    sol_words = set()
    for i in range(NUM_ROWS):
        for k in range(NUM_COLS):
            coord = Coordinate(i, k)
            search_for_words(coord, dtrie, {coord}, board, sol_words, "")

    return sol_words


# Tests
board = [
    ["A", "L", "B", "P"],
    ["C", "O", "E", "Y"],
    ["F", "C", "H", "P"],
    ["B", "A", "D", "A"]
]
words_in_board = {
    "AFOCAL", "CHAPEL", "CLOCHE", "DHOLE", "LOCHE", "CHOLA", "CHELA",
    "HOLEY", "FOCAL", "FOLEY", "COLEY", "COLBY", "COHAB", "COBLE", "DACHA",
    "BACHA", "BACCO", "BACCA", "BLECH", "PHOCA", "ALOHA", "ALEPH", "CHAPE",
    "BOCCA", "BOCCE", "BOCHE", "LECH", "PECH", "OCHE", "FOAL", "YECH", "OBEY",
    "YEBO", "LOCA", "LOBE", "LOCH", "HYPE", "HELO", "PELA", "HOLE", "COCA"}
words_not_in_board = {
    "DUMMY", "WORDS", "FOR", "TESTING"
}
dictionary = words_in_board | words_not_in_board

found_words = solve_boggle(board, dictionary)

assert found_words == words_in_board
