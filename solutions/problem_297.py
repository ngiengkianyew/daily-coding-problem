from typing import Dict, List


def minimize_drinks(drinks, remaining_drinks, remaining_customers, cust_by_drink):
    min_option = drinks

    if not remaining_customers:
        return drinks - remaining_drinks

    for drink in remaining_drinks:
        option = minimize_drinks(
            drinks, remaining_drinks - {drink},
            remaining_customers - cust_by_drink[drink], cust_by_drink)
        if len(option) < len(min_option):
            min_option = option

    return min_option


def get_min_drinks(preferences: Dict[int, List[int]]):
    cust_by_drink = dict()
    for cust in preferences:
        for drink in preferences[cust]:
            if drink not in cust_by_drink:
                cust_by_drink[drink] = set()
            cust_by_drink[drink].add(cust)

    remaining_drinks = set(cust_by_drink.keys())
    remaining_customers = set(preferences.keys())
    min_drinks = minimize_drinks(set(cust_by_drink.keys()), remaining_drinks,
                                 remaining_customers, cust_by_drink)
    return min_drinks


# Tests
preferences = {
    0: [0, 1, 3, 6],
    1: [1, 4, 7],
    2: [2, 4, 7, 5],
    3: [3, 2, 5],
    4: [5, 8]
}
assert get_min_drinks(preferences) == {1, 5}
