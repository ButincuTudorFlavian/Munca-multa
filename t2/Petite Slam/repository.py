import os
from domain import Player

class PlayerRepository:
    """
    Manages the logic for the Petite Slam tennis tournament.
    """

    def __init__(self, filename):
        self._filename = filename

    def load_players(self):
        """
        Reads player data from a text file.
        Expected format: id,name,strength
        """

        player_list = []
        if not os.path.exists(self._filename):
            return []

        with open(self._filename, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    p = Player(parts[0].strip(), parts[1].strip(), parts[2].strip())
                    player_list.append(p)
        return player_list