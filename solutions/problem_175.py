from random import random
import bisect


def get_transition_map(transition_probs):
    transition_map = dict()
    for source, target, prob in transition_probs:
        if source not in transition_map:
            transition_map[source] = ([], [])

        if not transition_map[source][0]:
            transition_map[source][0].append(prob)
        else:
            prev_prob = transition_map[source][0][-1]
            transition_map[source][0].append(prev_prob + prob)
        transition_map[source][1].append(target)

    return transition_map


def get_new_state(state_trans_probs):
    rand = random()
    probs, states = state_trans_probs
    index = bisect.bisect(probs, rand)

    return states[index]


def calculate_visits(start_state, transition_probs, steps):
    transition_map = get_transition_map(transition_probs)

    visit_counter = dict()
    for state in transition_map:
        visit_counter[state] = 0

    for _ in range(steps):
        visit_counter[start_state] += 1

        state_trans_probs = transition_map[start_state]
        start_state = get_new_state(state_trans_probs)

    return visit_counter


# Tests
transition_probs = [
    ('a', 'a', 0.9),
    ('a', 'b', 0.075),
    ('a', 'c', 0.025),
    ('b', 'a', 0.15),
    ('b', 'b', 0.8),
    ('b', 'c', 0.05),
    ('c', 'a', 0.25),
    ('c', 'b', 0.25),
    ('c', 'c', 0.5)
]
visit_counter = calculate_visits('a', transition_probs, 50000)
assert visit_counter['a'] > visit_counter['b']
assert visit_counter['a'] > visit_counter['c']
assert visit_counter['b'] > visit_counter['c']
