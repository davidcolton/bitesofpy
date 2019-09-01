from collections import namedtuple
from datetime import datetime

Transaction = namedtuple("Transaction", "giver points date")
Transaction.__new__.__defaults__ = (datetime.now(),)  # http://bit.ly/2rmiUrL


class User:
    def __init__(self, name):
        self._name = name
        self.__transactions = []
        self._karma = 0
        self._fans = set()
        self._points = []

    @property
    def name(self):
        return self._name

    @property
    def _transactions(self):
        return self.__transactions

    @property
    def karma(self):
        return self._karma

    @property
    def fans(self):
        return len(self._fans)

    @property
    def points(self):
        if len(self._points) == 1:
            return self._points
        else:
            return [min(self._points), max(self._points)]

    def __add__(self, trxn):
        giver, points, given = trxn
        self._karma += points
        self._fans.add(giver)
        self._points.append(points)
        return self

    def __str__(self):
        fan_str = "fan"
        if self.fans > 1:
            fan_str += "s"
        return f"{self.name} has a karma of {self.karma} and {self.fans} {fan_str}"
