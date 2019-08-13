from bisect import bisect


class OrderedList:

    def __init__(self):
        self._numbers = []

    def add(self, num):
        idx = bisect(self._numbers, num)
        return self._numbers.insert(idx, num)

    def __str__(self):
        return ', '.join(str(num) for num in self._numbers)