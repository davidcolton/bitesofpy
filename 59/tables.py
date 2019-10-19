import numpy as np


class MultiplicationTable:
    def __init__(self, length):
        """Create a 2D self._table of (x, y) coordinates and
           their calculations (form of caching)"""
        self.x = length
        self.y = length
        self.area = self.x * self.y

        # Create a list of lists to represent the table
        self.table = []
        for row in range(1, self.x + 1):
            self.table.append([row * col for col in range(1, self.y + 1)])

    def __len__(self):
        """Returns the area of the table (len x* len y)"""
        return self.area

    def __str__(self):
        """Returns a string representation of the table"""
        return_str = ""
        for row in self.table:
            return_str += " | ".join(str(x) for x in row) + " \n"
        return return_str

    def calc_cell(self, x, y):
        """Takes x and y coords and returns the (pre-calculated) result"""
        return self.table[x - 1][y - 1]
