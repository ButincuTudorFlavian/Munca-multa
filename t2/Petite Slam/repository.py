import os
from domain import Player

class PlayerRepository:
    """
    Manages the logic for the Petite Slam tennis tournament.
    """

    def __init__(self, filename):
        self.players = self.load_players(filename)

    def load_players(self, filename):
        """
        Reads player data from a text file.
        Expected format: id,name,strength
        """

        player_list = []
        if not os.path.exists(filename):
            return []

        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    p = Player(parts[0].strip(), parts[1].strip(), parts[2].strip())
                    player_list.append(p)
        return player_list