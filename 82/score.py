from enum import Enum

THUMBS_UP = "👍"  # in case you go f-string ...


class Score(Enum):
    BEGINNER = 2
    INTERMEDIATE = 3
    ADVANCED = 4
    CHEATED = 1

    def __str__(self):
        return f"{self.name} => {self.value * THUMBS_UP}"

    @classmethod
    def average(cls):
        sum = 0
        for count, s in enumerate(cls, 1):
            sum += s.value
        return sum / count

