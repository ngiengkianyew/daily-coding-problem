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


def calculate_intersect_area(r1, r2):
    if r1.tl.y > r2.tl.y:
        y_inter_up = r2.tl.y
        y_inter_lo = r1.br.y
    else:
        y_inter_up = r1.tl.y
        y_inter_lo = r2.br.y
    print(y_inter_up, y_inter_lo)
    height = max(0, y_inter_up - y_inter_lo)
    print("height:", height)

    if r1.tl.x < r2.tl.x:
        x_inter_le = r2.tl.x
        x_inter_ri = r1.br.x
    else:
        x_inter_le = r1.tl.x
        x_inter_ri = r2.br.x
    print(x_inter_le, x_inter_ri)
    width = max(0, x_inter_ri - x_inter_le)
    print("width:", width)

    area = height * width
    print(area)

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
