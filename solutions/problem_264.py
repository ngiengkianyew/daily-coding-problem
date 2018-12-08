# NOTE: The answer in the problem description is incorrect since
# it doesn't include '100' or '110'


def generate_combos(chars, k, context=""):
    if not k:
        return set([context])

    combos = set()
    for ch in chars:
        combos |= generate_combos(chars, k-1, context + ch)

    return combos


def get_debruijn_seq(chars, combos, context=""):
    if not combos:
        return set([context])

    dseqs = set()
    if not context:
        for cb in combos:
            child_dseqs = get_debruijn_seq(
                chars, combos - set([cb]), cb)
            dseqs |= child_dseqs

        return dseqs

    for ch in chars:
        new_cb = context[-2:] + ch
        if new_cb in combos:
            child_dseqs = get_debruijn_seq(
                chars, combos - set([new_cb]), context + ch)
            dseqs |= child_dseqs

    return dseqs


# Tests
c, k = {'0', '1'}, 3
combos = generate_combos(c, k)
dseqs = get_debruijn_seq(c, combos)
assert all([all([cb in ds for cb in combos]) for ds in dseqs])
