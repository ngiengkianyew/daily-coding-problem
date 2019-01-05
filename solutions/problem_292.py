class Group:
    def __init__(self):
        self.members = set()
        self.enemies = set()

    def __repr__(self):
        return str(self.members)

    def add_student(self, student, enemies):
        self.members.add(student)
        self.enemies |= set(enemies)


def get_groups(enemy_map):
    students = enemy_map.keys()
    first, second = Group(), Group()
    for student in students:
        if not first.members:
            first.add_student(student, enemy_map[student])
        elif student not in first.enemies:
            first.add_student(student, enemy_map[student])
        elif not second.members:
            second.add_student(student, enemy_map[student])
        elif student not in second.enemies:
            second.add_student(student, enemy_map[student])

    if len(first.members) + len(second.members) == len(students):
        return first.members, second.members

    return False


# Tests
enemy_map = {
    0: [3],
    1: [2],
    2: [1, 4],
    3: [0, 4, 5],
    4: [2, 3],
    5: [3]
}
assert get_groups(enemy_map) == ({0, 1, 4, 5}, {2, 3})

enemy_map = {
    0: [3],
    1: [2],
    2: [1, 3, 4],
    3: [0, 2, 4, 5],
    4: [2, 3],
    5: [3]
}
assert get_groups(enemy_map) == False
