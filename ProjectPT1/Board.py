"""
Quoridor II Board Data Class

Author: Troy Caro <twc9438@rit.edu>
"""

from .square import Square


class BoardData(object):
    """Class containing the matrix of Square objects, and the
    list of wall locations on the board."""

    __slots__ = ('data', 'walls')

    def __init__(self, row, col):
        grid = []
        for r in range(row):
            grid.append([])
            for c in range(col):
                grid[r].append(c)
        self.data = grid

        for x in range(row):
            for y in range(col):
                self.data[x][y] = Square()
        self.walls = []

    def build(self, row, col):
        for x in range(row):
            for y in range(col):
                if (x - 1 >= 0):
                    self.data[x][y].neighbors.append([x - 1, y])
                if (x + 1 != row):
                    self.data[x][y].neighbors.append([x + 1, y])
                if (y - 1 >= 0):
                    self.data[x][y].neighbors.append([x, y - 1])
                if (y + 1 != col):
                    self.data[x][y].neighbors.append([x, y + 1])
