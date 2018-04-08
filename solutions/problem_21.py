def get_num_classrooms(timing_tuples):
    if not timing_tuples:
        return 0

    start_times = dict()
    end_times = dict()
    for start, end in timing_tuples:
        if start not in start_times:
            start_times[start] = 0
        start_times[start] += 1

        if end not in end_times:
            end_times[end] = 0
        end_times[end] += 1

    global_start, global_end = min(start_times), max(end_times)

    max_class_count = 0
    current_class_count = 0
    for i in range(global_start, global_end):
        if i in start_times:
            current_class_count += start_times[i]
            if current_class_count > max_class_count:
                max_class_count = current_class_count
        if i in end_times:
            current_class_count -= end_times[i]

    return max_class_count


assert get_num_classrooms([]) == 0
assert get_num_classrooms([(30, 75), (0, 50), (60, 150)]) == 2
assert get_num_classrooms([(30, 75), (0, 50), (10, 60), (60, 150)]) == 3
assert get_num_classrooms([(60, 150)]) == 1
assert get_num_classrooms([(60, 150), (150, 170)]) == 2
assert get_num_classrooms([(60, 150), (60, 150), (150, 170)]) == 3
