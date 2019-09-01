scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
ranks = "white yellow orange green blue brown black paneled red".split()
BELTS = dict(zip(scores, ranks))


class NinjaBelt:
    def __init__(self, score=0):
        self._score = score
        self._last_earned_belt = None

    def _get_belt(self, new_score):
        """Might be a useful helper"""
        return BELTS[
            max([threshold for threshold in BELTS.keys() if threshold <= new_score])
        ]

    def _get_score(self):
        return self._score

    def _set_score(self, new_score):
        if isinstance(new_score, int) and new_score > self._score:
            self._score = new_score
            belt_test = self._get_belt(self._score)
            if self._last_earned_belt == belt_test:
                print(f"Set new score to {self._score}")
            else:
                self._last_earned_belt = belt_test
                print(
                    f"Congrats, you earned {self._score}",
                    "points obtaining the PyBites Ninja",
                    f"{self._last_earned_belt.capitalize()} Belt",
                    sep=" ",
                )
        else:
            raise ValueError

    score = property(_get_score, _set_score)
