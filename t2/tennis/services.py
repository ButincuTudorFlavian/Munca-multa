from repository import TextFileTennisPlayerRepo
import random

class TennisService:
    def __init__(self, tennis_repo: TextFileTennisPlayerRepo):
        self._tennis_repo = tennis_repo

    def list_all_players(self):
        return self._tennis_repo.list_all_players()

    def list_all_players_descending(self):
        sorted_players = sorted(self.list_all_players(), key=lambda player: player.get_strength, reverse=True)
        return sorted_players

    def player_loses(self, player_id):
        return self._tennis_repo.delete_player(player_id)

    def player_wins(self, player_id):
        for player in self.list_all_players():
            if player.get_id == player_id:
                player.set_strength += 1

    def paired_players(self):
        sorted_players = sorted(self.list_all_players(), key=lambda player: player.get_strength)
        number = self.no_of_players()
        selected_players = sorted_players[:number]
        random.shuffle(selected_players)
        paired_players = [selected_players[i:i+2] for i in range(0, len(selected_players), 2)]
        return paired_players

    def is_qualify_round(self):
        number_of_players = len(self.list_all_players())
        p2 = 2
        while p2 < number_of_players:
            p2 = p2 * 2
        if p2 == number_of_players:
            return False
        return True

    def no_of_players(self):
        number_of_players = len(self.list_all_players())
        p2 = 2
        while p2 < number_of_players:
            p2 = p2 * 2
        p2 = p2 // 2
        number_ok = (number_of_players - p2) * 2
        return number_ok