"""
Quoridor II: Class for each square on the board.

Author: Troy Caro <twc9438@rit.edu>
"""


class Square(object):
    """Class representing a square on the game board"""

    __slots__ = ('neighbors')

    def __init__(self):
        self.neighbors = []
