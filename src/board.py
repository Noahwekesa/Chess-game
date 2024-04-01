from const import *
from square import Square


class Board:
    def __init__(self):
        # 2d array
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]

        self._create()

    def _create(self):
        # looping thru the 2d array
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):
        pass
