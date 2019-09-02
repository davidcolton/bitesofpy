from statistics import mean
from statistics import median
from decimal import Decimal


class IntList(list):
    def __init__(self, item):
        super().__init__(item)

    @property
    def mean(self):
        return mean(self)

    @property
    def median(self):
        return median(self)

    def append(self, item):
        item = self.validate(item)
        super().append(item)

    def __add__(self, item):
        item = self.validate(item)
        super().__add__(item)

    def __iadd__(self, item):
        item = self.validate(item)
        super().__iadd__(item)
        return self

    def validate(self, item):
        if isinstance(item, (int, float, Decimal)):
            return int(item)
        elif isinstance(item, list):
            if all(isinstance(v, (int, float, Decimal)) for v in item):
                return [int(x) for x in item]
            else:
                raise TypeError
        else:
            raise TypeError

