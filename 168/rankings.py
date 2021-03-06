from dataclasses import dataclass
from typing import List, Tuple
import heapq

# https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/

bites: List[int] = [283, 282, 281, 263, 255, 230, 216, 204, 197, 196, 195]
names: List[str] = [
    "snow",
    "natalia",
    "alex",
    "maquina",
    "maria",
    "tim",
    "kenneth",
    "fred",
    "james",
    "sara",
    "sam",
]


@dataclass
class Ninja:
    """
    The Ninja class will have the following features:

    string: name
    integer: bites
    support <, >, and ==, based on bites
    print out in the following format: [469] bob
    """

    name: str
    bites: int

    def __str__(self):
        return f"[{self.bites}] {self.name}"

    def __lt__(self, other):
        return self.bites < other.bites


@dataclass
class Rankings:
    """
    The Rankings class will have the following features:

    method: add() that adds a Ninja object to the rankings
    method: dump() that removes/dumps the lowest ranking Ninja from Rankings
    method: highest() returns the highest ranking Ninja, but it takes an optional
            count parameter indicating how many of the highest ranking Ninjas to return
    method: lowest(), the same as highest but returns the lowest ranking Ninjas, also
            supports an optional count parameter
    returns how many Ninjas are in Rankings when len() is called on it
    method: pair_up(), pairs up study partners, takes an optional count
            parameter indicating how many Ninjas to pair up
    returns List containing tuples of the paired up Ninja objects
    """

    def __init__(self):
        self.rankings = []
        heapq.heapify(self.rankings)

    def __len__(self):
        return len(self.rankings)

    def add(self, ninja):
        heapq.heappush(self.rankings, ninja)

    def dump(self):
        return heapq.heappop(self.rankings)

    def highest(self, num=1):
        return heapq.nlargest(num, self.rankings)

    def lowest(self, num=1):
        return heapq.nsmallest(num, self.rankings)

    def pair_up(self, num=3):
        largest = self.highest(num)
        smallest = self.lowest(num)
        return list(zip(largest, smallest))
