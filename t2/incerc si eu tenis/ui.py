from texttable import Texttable

class ConsoleUI:
    def __init__(self, services):
        self._services = services

    def game_start(self):
        player_list = self._services.list_players()

        main = Texttable()
        main.header([" "])
        for player in player_list:
            main.add_row([player])

        print("All the players in the game: ")
        print(main.draw())

        input("Press enter to start the game")


    def first_time(self):
        player_list = self._services.list_players()
        number = player_list.length()

def get_closest_power_of_2(number):
    