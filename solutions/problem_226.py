def update_letter_order(sorted_words, letters):
    order = list()
    new_words = dict()
    prev_char = None
    for word in sorted_words:
        if word:
            char = word[0]
            if char != prev_char:
                order.append(char)
            if char not in new_words:
                new_words[char] = list()
            new_words[char].append(word[1:])
            prev_char = char

    for index, char in enumerate(order):
        letters[char] |= set(order[index + 1:])

    for char in new_words:
        update_letter_order(new_words[char], letters)


def find_path(letters, start, path, length):
    if len(path) == length:
        return path

    if not letters[start]:
        return None

    for next_start in letters[start]:
        new_path = find_path(letters, next_start, path + [next_start], length)
        if new_path:
            return new_path


def update_letter_order_helper(sorted_words):
    letters = dict()
    for word in sorted_words:
        for letter in word:
            if letter not in letters:
                letters[letter] = set()

    update_letter_order(sorted_words, letters)

    max_children = max([len(x) for x in letters.values()])
    potential_heads = [x for x in letters if len(letters[x]) == max_children]

    path = None
    for head in potential_heads:
        path = find_path(letters, head, path=[head], length=len(letters))
        if path:
            break

    return path


# Tests
assert update_letter_order_helper(
    ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz']) == ['x', 'z', 'w', 'y']
