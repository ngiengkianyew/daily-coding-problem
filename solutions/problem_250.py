def get_num_from_string(char_map, string):
    power = 0
    total = 0
    for char in string[::-1]:
        total += char_map[char] * (10 ** power)
        power += 1

    return total


def is_valid_map(exp1, exp2, res, char_map):
    num1 = get_num_from_string(char_map, exp1)
    num2 = get_num_from_string(char_map, exp2)
    num3 = get_num_from_string(char_map, res)
    return num1 + num2 == num3


def evaluate_char_maps(exp1, exp2, res, char_maps):
    for char_map in char_maps:
        if is_valid_map(exp1, exp2, res, char_map):
            return char_map


def assign_letters(chars_left, nums_left, restrictions, char_map=dict()):
    if not chars_left:
        return [char_map]

    curr_char = list(chars_left)[0]
    char_maps = list()
    for num in nums_left:
        if num in restrictions[curr_char]:
            continue

        char_map_cp = char_map.copy()
        char_map_cp[curr_char] = num

        child_char_maps = assign_letters(
            chars_left - set([curr_char]),
            nums_left - set([num]),
            restrictions,
            char_map_cp)
        char_maps.extend(child_char_maps)

    return char_maps


def decode(exp1, exp2, res):
    characters = set(exp1) | set(exp2) | set(res)
    assert len(characters) < 11
    nums = set(range(0, 10))

    restrictions = dict()
    for char in characters:
        restrictions[char] = set()
    for word in [exp1, exp2, res]:
        restrictions[word[0]].add(0)

    char_maps = assign_letters(characters, nums, restrictions)
    return evaluate_char_maps(exp1, exp2, res, char_maps)


# Tests
assert decode("SEND", "MORE", "MONEY") == {
    'S': 9, 'E': 5, 'N': 6, 'D': 7, 'M': 1, 'O': 0, 'R': 8, 'Y': 2}
