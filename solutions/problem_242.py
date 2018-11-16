class HourlySubscribers:
    def __init__(self):
        self.subscribers = [0] * 24

    def update(self, hour, value):
        self.subscribers[hour] += value

    def query(self, start, end):
        return sum(self.subscribers[start:end])


# Tests
hs = HourlySubscribers()
hs.update(2, 50)
hs.update(5, 110)
assert hs.query(1, 7) == 160
