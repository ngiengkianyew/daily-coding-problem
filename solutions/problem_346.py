import sys


def get_city_map(flights):
    city_map = dict()
    for src, dst, fare in flights:
        if dst not in city_map:
            city_map[dst] = list()
        city_map[dst].append((src, fare))

    return city_map


def get_cheapest_fare(src, tgt, max_stops, city_map, total=0, stops=0):
    if stops > max_stops:
        return sys.maxsize

    if src == tgt:
        return total

    new_tgt_fares = city_map[tgt]
    possibilities = list()
    for new_tgt, fare in new_tgt_fares:
        poss = get_cheapest_fare(
            src, new_tgt, max_stops, city_map, total + fare, stops + 1)
        possibilities.append(poss)

    return min(possibilities)


# Tests
flights = [
    ('JFK', 'ATL', 150),
    ('ATL', 'SFO', 400),
    ('ORD', 'LAX', 200),
    ('LAX', 'DFW', 80),
    ('JFK', 'HKG', 800),
    ('ATL', 'ORD', 90),
    ('JFK', 'LAX', 500),
]
city_map = get_city_map(flights)
assert get_cheapest_fare("JFK", "LAX", 3, city_map) == 440
assert get_cheapest_fare("JFK", "LAX", 0, city_map) == sys.maxsize
