digit_mapping = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f']
}


def get_letter_strings(number_string):
    if not number_string:
        return

    if len(number_string) == 1:
        return digit_mapping[number_string[0]]

    possible_strings = list()
    current_letters = digit_mapping[number_string[0]]
    strings_of_rem_nums = get_letter_strings(number_string[1:])
    for letter in current_letters:
        for string in strings_of_rem_nums:
            possible_strings.append(letter + string)

    return possible_strings


assert get_letter_strings("2") == [
    'a', 'b', 'c']
assert get_letter_strings("23") == [
    'ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
assert get_letter_strings("32") == [
    'da', 'db', 'dc', 'ea', 'eb', 'ec', 'fa', 'fb', 'fc']
