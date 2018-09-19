class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "(x={},y={})".format(self.x, self.y)


class Rectangle:
    def __init__(self, json):
        self.tl = Point(json["top_left"][0], json["top_left"][1])
        width, height = json["dimensions"]
        self.br = Point(self.tl.x + width, self.tl.y - height)

    def __repr__(self):
        return "(tl={},br={})".format((self.tl), (self.br))

    def get_area(self):
        return (self.br.x - self.tl.x) * (self.tl.y - self.br.y)

    def envelopes(self, other):
        return self.tl.x < other.tl.x and self.tl.y > other.tl.y and \
            self.br.x > other.br.x and self.br.y < other.br.y

    def is_disjoint_with(self, other):
        return self.br.y > other.tl.y or other.br.y > self.tl.y or \
            self.tl.x > other.br.x or other.tl.x > self.br.x


def calculate_intersect_area(r1, r2):
    if r1.envelopes(r2):
        area = r2.get_area()
    elif r2.envelopes(r1):
        area = r1.get_area()
    elif r1.is_disjoint_with(r2) or r2.is_disjoint_with(r1):
        area = 0
    else:
        heights = list(sorted([r1.tl.y, r1.br.y, r2.tl.y, r2.br.y]))[1:-1]
        height = heights[1] - heights[0]
        widths = list(sorted([r1.tl.x, r1.br.x, r2.tl.x, r2.br.x]))[1:-1]
        width = widths[1] - widths[0]
        area = height * width

    return area


# Tests
r1 = Rectangle({"top_left": (1, 4), "dimensions": (3, 3)})
r2 = Rectangle({"top_left": (0, 5), "dimensions": (4, 3)})
assert calculate_intersect_area(r1, r2) == 6

r1 = Rectangle({"top_left": (1, 1), "dimensions": (1, 1)})
r2 = Rectangle({"top_left": (5, 5), "dimensions": (1, 1)})
assert calculate_intersect_area(r1, r2) == 0

r1 = Rectangle({"top_left": (0, 5), "dimensions": (5, 5)})
r2 = Rectangle({"top_left": (1, 4), "dimensions": (2, 2)})
assert calculate_intersect_area(r1, r2) == 4

r1 = Rectangle({"top_left": (0, 5), "dimensions": (5, 5)})
r2 = Rectangle({"top_left": (4, 4), "dimensions": (3, 3)})
assert calculate_intersect_area(r1, r2) == 3
