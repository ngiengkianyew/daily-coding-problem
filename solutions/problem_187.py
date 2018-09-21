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

    def envelopes(self, other):
        return self.tl.x <= other.tl.x and self.tl.y >= other.tl.y and \
            self.br.x >= other.br.x and self.br.y <= other.br.y


def contains_overlapping_pair(rectangles):

    for i in range(len(rectangles) - 1):
        for j in range(i + 1, len(rectangles)):
            if rectangles[i].envelopes(rectangles[j]) or \
                    rectangles[j].envelopes(rectangles[i]):
                return True

    return False


# Tests

# example provided in the question is incorrect
r1 = Rectangle({"top_left": (1, 4), "dimensions": (3, 3)})
r2 = Rectangle({"top_left": (-1, 3), "dimensions": (2, 1)})
r3 = Rectangle({"top_left": (0, 5), "dimensions": (4, 4)})
assert contains_overlapping_pair([r1, r2, r3])

r1 = Rectangle({"top_left": (1, 4), "dimensions": (3, 3)})
r2 = Rectangle({"top_left": (-1, 3), "dimensions": (2, 1)})
r3 = Rectangle({"top_left": (0, 5), "dimensions": (4, 3)})
assert not contains_overlapping_pair([r1, r2, r3])
