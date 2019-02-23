import sys


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "[x={},y={}]".format(self.x, self.y)


def get_distance(p1, p2):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


def get_closest(point_tuples):
    points = [Point(x, y) for (x, y) in point_tuples]
    min_dist, min_dist_pts = sys.maxsize, None
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            dist = get_distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                min_dist_pts = ((points[i].x, points[i].y),
                                (points[j].x, points[j].y))

    return min_dist_pts


# Tests
assert get_closest([(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)]) == \
    ((1, 1), (-1, -1))
