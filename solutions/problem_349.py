cons_repl = [
    (["b", "f", "p", "v"], 1),
    (["c", "g", "j", "k", "q", "s", "x", "z"], 2),
    (["d", "t"], 3),
    (["m", "n"], 5),
    (["l"], 4),
    (["r"], 6),
]
sim_cons = [
    {"c", "k", "s"}
]
vowel_like = {"a", "e", "i", "o", "u", "y", "w", "h"}


def build_cons_repl_map(cons_repl):
    cons_repl_map = dict()
    for chars, num in cons_repl:
        for char in chars:
            cons_repl_map[char] = num
    return cons_repl_map


def build_cons_like_map(sim_cons):
    cons_like_map = dict()
    for group in sim_cons:
        elect = min(group)
        for char in group:
            cons_like_map[char] = elect

    return cons_like_map


def soundexify(word, cons_repl_map, cons_like_map):
    word = word.lower()

    # deduplicate similar sounding consonants
    w1 = ""
    for char in word:
        if char in cons_like_map:
            char = cons_like_map[char]
        if w1 and char == w1[-1]:
            continue
        w1 += char

    # remove vowel like characters
    w2 = ""
    for char in w1[1:]:
        if char not in vowel_like:
            w2 += char
    w3 = ""

    # replace consonants with numbers
    for char in w2:
        w3 += str(cons_repl_map[char])

    # massage into final format
    w3 += "000"
    w3 = w3[:3]
    final = w1[0] + w3

    return final


# Test
cons_repl_map = build_cons_repl_map(cons_repl)
cons_like_map = build_cons_like_map(sim_cons)
c1 = soundexify("Jackson", cons_repl_map, cons_like_map)
c2 = soundexify("Jaxen", cons_repl_map, cons_like_map)
assert c1 == c2
assert c1 == "j250"
