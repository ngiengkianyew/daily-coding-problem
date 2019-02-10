class EloRatings:
    START_RATING = 1000

    def __init__(self):
        self.ratings = dict()

    def add_player(self, name):
        self.ratings[name] = EloRatings.START_RATING

    def add_result(self, p1, p2, winner):
        if p1 not in self.ratings:
            self.add_player(p1)
        if p2 not in self.ratings:
            self.add_player(p2)

        if not winner:
            if self.ratings[p1] == self.ratings[p2]:
                return

            diff = self.ratings[p1] // 20 \
                if self.ratings[p1] > self.ratings[p2] \
                else -self.ratings[p2] // 20

            self.ratings[p1] -= diff
            self.ratings[p2] += diff
        else:
            loser = p2 if winner == p1 else p1
            diff = self.ratings[loser] // 10
            self.ratings[loser] -= diff
            self.ratings[winner] += diff


# Tests
elo = EloRatings()
elo.add_player("a")
elo.add_player("b")
elo.add_player("c")
elo.add_result("a", "b", "a")
elo.add_result("a", "b", "b")
elo.add_result("a", "b", None)
