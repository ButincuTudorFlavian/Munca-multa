from repository import TextFileTennisPlayerRepo
from services import TennisService

class UI:
    def __init__(self, tennis_service: TennisService):
        self._tennis_service = tennis_service
        self.running = True

    @staticmethod
    def print_menu():
        print("Welcome to Tennis Tournament!")
        print("   1. List all players")
        print("   2. Start a Tennis tournament")
        print("   x. Exit")

    @staticmethod
    def run():
        try:
            tennis_repo = TextFileTennisPlayerRepo()
            tennis_service = TennisService(tennis_repo)
            return UI(tennis_service)
        except Exception as e:
            print(e)
            return None

    def user_run(self):
        if self._tennis_service is None:
            return

        while self.running:
            self.print_menu()
            option = input("Enter your choice: ")
            if option == "1":
                try:
                    self.list_all_players()
                except Exception as e:
                    print(e)
            elif option == "2":
                self.play_game()
            else:
                self.running = False

    def list_all_players(self):
        player_list = self._tennis_service.list_all_players_descending()
        print("Displaying all players: ")
        for player in player_list:
            print(player)

    def game(self, paired_players):
        for players in paired_players:
            player1 = players[0].get_name
            player2 = players[1].get_name
            print(players[0])
            print(players[1])
            player_win = input(f"{player1} vs {player2}. Who wins?\n")
            if player_win == player1:
                self._tennis_service.player_loses(players[1].get_id)
                self._tennis_service.player_wins(players[0].get_id)
            else:
                self._tennis_service.player_loses(players[0].get_id)
                self._tennis_service.player_wins(players[1].get_id)

    def qualify(self):
        print("---- Welcome to the qualifications for the Tennis Tournament!")
        paired_players = self._tennis_service.paired_players()
        self.game(paired_players)
        self.tournament()

    def tournament(self):
        print("---- Welcome to the game of the Tennis Tournament!")
        paired_players = self._tennis_service.paired_players()
        while len(paired_players) > 1:
            if len(paired_players) == 4:
                print("Last 8\n")
            if len(paired_players) == 2:
                print("Last 4\n")
            self.game(paired_players)
            paired_players = self._tennis_service.paired_players()

        for players in paired_players:
            player1 = players[0].get_name
            player2 = players[1].get_name
            print(players[0])
            print(players[1])
            final_win = input(f"Final: {player1} vs {player2}. Who wins?\n")
            print(f"Player {final_win} wins the tournament\n")

    def play_game(self):
        if self._tennis_service.is_qualify_round() is True:
            self.qualify()
        else:
            self.tournament()

if __name__ == "__main__":
    ui = UI.run()
    if ui is not None:
        ui.user_run()