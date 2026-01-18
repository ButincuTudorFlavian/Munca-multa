import string

from services import Game


class UI:
    def __init__(self):
        self.game = Game()

    def coord_to_index(self, coord):
        col = string.ascii_uppercase.index(coord[0])
        row = int(coord[1]) - 1
        return row, col

    def place_player_ships(self):
        print("Place your ships (example: A1 H)")
        while len(self.game.player_board.ships) < self.game.player_board.SHIP_COUNT:
            print(self.game.player_board)
            data = input(">> ").upper().split()

            if len(data) != 2:
                print("Invalid input!")
                continue

            coord, orientation = data
            try:
                row, col = self.coord_to_index(coord)
            except:
                print("Invalid coordinate!")
                continue

            if not self.game.player_board.place_ship(row, col, orientation):
                print("Cannot place ship here!")

    def player_fire(self):
        coord = input("fire: ").upper()
        try:
            row, col = self.coord_to_index(coord)
        except:
            print("Invalid coordinate!")
            return

        self.game.computer_board.receive_fire(row, col)
        self.game.targeting_board.receive_fire(row, col)
        if self.game.computer_board.receive_fire(row, col) == 2:
            print("HIT!")
        else:
            print("MISSED!")

    def start(self):
        self.place_player_ships()

        while True:
            print("\nYour board:")
            print(self.game.player_board)
            print("\nTargeting board:")
            print(self.game.targeting_board)

            self.player_fire()

            if self.game.computer_board.all_ships_sunk():
                print("YOU WIN!")
                break

            self.game.computer_fire()

            if self.game.player_board.all_ships_sunk():
                print("COMPUTER WINS!")
                break
