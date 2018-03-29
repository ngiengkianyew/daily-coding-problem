def get_step_combos(num_steps, step_sizes):
    combos = list()
    
    if num_steps < min(step_sizes):
        return combos
    
    for step_size in step_sizes:
        if num_steps == step_size:
            combos.append([step_size])
        elif num_steps > step_size:
            child_combos = get_step_combos(num_steps - step_size, step_sizes)
            for child_combo in child_combos:
                combos.append([step_size] + child_combo)
    return combos


assert get_step_combos(4, [1, 2]) == \
    [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2]]
assert get_step_combos(4, [1, 2, 3]) == \
    [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [1, 3], [2, 1, 1], [2, 2], [3, 1]]
