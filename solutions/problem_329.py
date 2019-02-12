def find_matches(guy_pref, gal_pref):
    if not guy_pref:
        return []

    matches = list()
    taken_guys, taken_gals = set(), set()
    for guy in guy_preferences:
        gal = guy_pref[guy][0]
        pref_guy = gal_pref[gal][0]
        if pref_guy == guy:
            matches.append((guy, gal))
            taken_guys.add(guy)
            taken_gals.add(gal)

    if not matches:
        for guy in guy_preferences:
            gal = guy_pref[guy][0]
            matches.append((guy, gal))
        return matches

    for (guy, gal) in matches:
        del guy_pref[guy]
        del gal_pref[gal]

        for rguy in guy_pref:
            guy_pref[rguy] = [x for x in guy_pref[rguy] if x not in taken_gals]
        for rgal in gal_pref:
            gal_pref[rgal] = [x for x in gal_pref[rgal] if x not in taken_guys]

    return matches + find_matches(guy_pref, gal_pref)


# Tests
guy_preferences = {
    'andrew': ['caroline', 'abigail', 'betty'],
    'bill': ['caroline', 'betty', 'abigail'],
    'chester': ['betty', 'caroline', 'abigail'],
}
gal_preferences = {
    'abigail': ['andrew', 'bill', 'chester'],
    'betty': ['bill', 'andrew', 'chester'],
    'caroline': ['bill', 'chester', 'andrew']
}
assert find_matches(guy_preferences, gal_preferences) == \
    [('bill', 'caroline'), ('andrew', 'abigail'), ('chester', 'betty')]
