def get_power_set(numbers):
    if len(numbers) == 0:
        return [set([])]

    power_set = list()

    current_number = numbers[0]
    child_power_set = get_power_set(numbers[1:])
    power_set.extend(child_power_set)

    for child_set in child_power_set:
        new_set = child_set.copy()
        new_set.add(current_number)
        power_set.append(new_set)

    return power_set


assert get_power_set([]) == [set()]
assert get_power_set([1]) == [set(), {1}]
assert get_power_set([1, 2]) == [set(), {2}, {1}, {1, 2}]
assert get_power_set([1, 2, 3]) == [
    set(), {3}, {2}, {2, 3}, {1}, {1, 3}, {1, 2}, {1, 2, 3}]
assert get_power_set([1, 2, 3, 4]) == [
    set(), {4}, {3}, {3, 4}, {2}, {2, 4}, {2, 3}, {2, 3, 4}, {1}, {1, 4},
    {1, 3}, {1, 3, 4}, {1, 2}, {1, 2, 4}, {1, 2, 3}, {1, 2, 3, 4}]
