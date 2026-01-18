from domain import PlayerBoard
import random

class Game():
    def __init__(self):
        self.player_board=PlayerBoard()
        self.computer_board=PlayerBoard()
        self.targeting_board=PlayerBoard()
        self.place_computer_ships()

    def place_computer_ships(self):
        while len(self.computer_board.ships) < self.computer_board.SHIP_COUNT:
            row = random.randint(0, 5)
            col = random.randint(0, 5)
            orientation = random.choice(['H', 'V'])
            self.computer_board.place_ship(row, col, orientation)

    def computer_fire(self):
        while True:
            row = random.randint(0, self.player_board.SIZE - 1)
            col = random.randint(0, self.player_board.SIZE - 1)


            if self.player_board.receive_fire(row, col) > 0:
                break
