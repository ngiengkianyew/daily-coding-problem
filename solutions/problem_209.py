# This solution generalizes to n strings

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def get_lcs(strings, context, indices):
    lcs_len = len(context)
    for letter in ALPHABET:
        new_indices = list()
        for j, string in enumerate(strings):
            index = string.find(letter, indices[j] + 1)
            if index == -1:
                break
            new_indices.append(index)
        if len(new_indices) == 3:
            length_cs = get_lcs(strings, context + letter, new_indices)
            if length_cs > lcs_len:
                lcs_len = length_cs

    return lcs_len


def get_lcs_helper(strings):
    return get_lcs(strings, "", [-1]*len(strings))


# Tests
assert get_lcs_helper(["epidemiologist", "refrigeration",
                       "supercalifragilisticexpialodocious"]) == 5
