import string

from texttable import Texttable

class Board():

    SIZE = 6
    def __init__(self):
        self.grid = []
        self.ships = []
        for row_index in range(self.SIZE):
            empty_row = []
            for col_index in range(self.SIZE):
                empty_row.append(' ')
            self.grid.append(empty_row)


    def receive_fire(self, row, col):
        if self.grid[row][col] in ('X', '.'):
            return 0

        if self.grid[row][col] == 'S':
            self.grid[row][col] = 'X'
            return 2

        if self.grid[row][col] == ' ':
            self.grid[row][col] = '.'
            return 1

    def all_ships_sunk(self):
        for row in self.grid:
            if 'S' in row:
                return False
        return True

    def __str__(self):
        t = Texttable()
        header = [" "] + list(string.ascii_uppercase[:self.SIZE])
        t.add_row(header)

        for i in range(self.SIZE):
            row = [i+1] + self.grid[i]
            t.add_row(row)

        return t.draw()

class PlayerBoard(Board):
    SHIP_LENGTH = 3
    SHIP_COUNT = 3
    def __init__(self):
        super().__init__()

    def can_place(self, row, col, orientation):
        if orientation not in ('H', 'V'):
            return False

        for i in range(self.SHIP_LENGTH):# row = 3 -_-_- col = 4
            if orientation == 'H':
                r, c = row, col + i
            elif orientation == 'V':
                r, c = row + i, col


            if r < 0 or r >= self.SIZE or c < 0 or c >= self.SIZE:
                return False


            if self.grid[r][c] != ' ':
                return False

        return True

    def place_ship(self, row, col, orientation):
        if not self.can_place(row, col, orientation):
            return False

        ship = []

        for i in range(self.SHIP_LENGTH):
            if orientation == 'H':
                r, c = row, col + i
            else:
                r, c = row + i, col

            self.grid[r][c] = 'S'
            ship.append((r, c))

        self.ships.append(ship)
        return True

