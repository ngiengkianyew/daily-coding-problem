import bisect


class TimedMap:
    def __init__(self):
        self.map = dict()

    def __repr__(self):
        return str(self.map)

    def setval(self, key, value, time):
        if key not in self.map:
            self.map[key] = ([time], [value])
            return

        times, values = self.map[key]
        insertion_point = bisect.bisect(times, time)
        times.insert(insertion_point, time)
        values.insert(insertion_point, value)

    def getval(self, key, time):
        if key not in self.map:
            return

        times, values = self.map[key]
        insertion_point = bisect.bisect(times, time)
        if not insertion_point:
            return

        return values[insertion_point - 1]


d = TimedMap()
d.setval(1, 1, 0)
d.setval(1, 2, 2)
assert d.getval(1, 1) == 1
assert d.getval(1, 3) == 2

d = TimedMap()
d.setval(1, 1, 5)
assert not d.getval(1, 0)
assert d.getval(1, 10) == 1

d = TimedMap()
d.setval(1, 1, 0)
d.setval(1, 2, 0)
assert d.getval(1, 0) == 2
