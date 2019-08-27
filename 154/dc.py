from dataclasses import dataclass


@dataclass(order=True)
class Bite:
    """Class for keeping track of an item in inventory."""

    number: int
    title: str
    level: str = "Beginner"

    def __post_init__(self):
        self.title = self.title.capitalize()
