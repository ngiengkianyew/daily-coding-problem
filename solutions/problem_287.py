from heapq import heappush


def get_similarity_score(users_a, users_b):
    union = users_a | users_b
    intersect = users_a & users_b

    return len(intersect) / len(union)


def get_similar_websites(visits, k=1):
    website_users = dict()
    for website, user in visits:
        if website not in website_users:
            website_users[website] = set()
        website_users[website].add(user)

    websites = list(website_users.keys())

    most_similar = list()
    for i in range(len(websites) - 1):
        for j in range(i + 1, len(websites)):
            web_a, web_b = websites[i], websites[j]
            sim_score = get_similarity_score(website_users[web_a], website_users[web_b])
            heappush(most_similar, (-sim_score, (web_a, web_b)))

    most_similar = [y for x, y in most_similar]

    return most_similar[:k]


# Tests
visits = [
    ("a", 1),
    ("a", 3),
    ("a", 5),
    ("b", 2),
    ("b", 6),
    ("c", 1),
    ("c", 2),
    ("c", 3),
    ("c", 4),
    ("c", 5),
    ("d", 4),
    ("d", 5),
    ("d", 6),
    ("d", 7),
    ("e", 1),
    ("e", 3),
    ("e", 5),
    ("e", 6),
]
assert get_similar_websites(visits, 1) == [("a", "e")]
assert get_similar_websites(visits, 3) == [("a", "e"), ("a", "c"), ("b", "d")]
