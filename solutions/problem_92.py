def get_course_order_helper(prereqs, indep, order):
    if not indep:
        return None, None, None
    elif not prereqs:
        return prereqs, indep, order

    new_indep = set()
    for dc in prereqs:
        required = prereqs[dc] - indep
        if not len(required):
            new_indep.add(dc)
            order.append(dc)

    for course in new_indep:
        del prereqs[course]

    return get_course_order_helper(prereqs, indep.union(new_indep), order)


def get_course_order(prereqs):

    indep = set()
    order = list()
    for course in prereqs:
        if not prereqs[course]:
            indep.add(course)
            order.append(course)
        else:
            prereqs[course] = set(prereqs[course])

    for course in indep:
        del prereqs[course]

    _, _, order = get_course_order_helper(prereqs, indep, order)

    return order


prereqs = {
    'CSC100': [],
    'CSC200': [],
    'CSC300': []
}
assert get_course_order(prereqs) == ['CSC100', 'CSC200', 'CSC300']

prereqs = {
    'CSC300': ['CSC100', 'CSC200'],
    'CSC200': ['CSC100'],
    'CSC100': []
}
assert get_course_order(prereqs) == ['CSC100', 'CSC200', 'CSC300']

prereqs = {
    'CSC400': ['CSC200'],
    'CSC300': ['CSC100', 'CSC200'],
    'CSC200': ['CSC100'],
    'CSC100': []
}
assert get_course_order(prereqs) == ['CSC100', 'CSC200', 'CSC400', 'CSC300']

prereqs = {
    'CSC400': ['CSC300'],
    'CSC300': ['CSC100', 'CSC200'],
    'CSC200': ['CSC100'],
    'CSC100': ['CSC400']
}
assert not get_course_order(prereqs)
