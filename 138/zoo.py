from itertools import count


class Animal:
    # Animal Counter
    ac = count(10001, 1)
    # List of Animals
    al = list()

    def __init__(self, name):
        self.name = name.title()
        self.num = next(self.ac)
        self.al.append(f"{self.num}. {self.name}")

    def __str__(self):
        return f"{self.num}. {self.name}"

    @classmethod
    def zoo(cls):
        the_zoo = "\n".join(cls.al)
        return the_zoo
