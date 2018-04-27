def get_itinerary(flights, starting_point, current_itinerary):
    # print("flights", flights)
    # print("starting_point", starting_point)
    # print("current_itinerary", current_itinerary)

    if not flights:
        return current_itinerary + [starting_point]

    updated_itinerary = None
    for index, (city_1, city_2) in enumerate(flights):
        if starting_point == city_1:
            child_itinerary = get_itinerary(
                flights[:index] + flights[index + 1:], city_2, current_itinerary + [city_1])
            if child_itinerary:
                if not updated_itinerary or "".join(child_itinerary) < "".join(updated_itinerary):
                    updated_itinerary = child_itinerary

    # print(updated_itinerary)

    return updated_itinerary


assert get_itinerary([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'),
                      ('HKO', 'ORD')], "YUL", []) == ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']
assert not get_itinerary([('SFO', 'COM'), ('COM', 'YYZ')], "YUL", [])
assert get_itinerary([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], "A", []) == [
    'A', 'B', 'C', 'A', 'C']
