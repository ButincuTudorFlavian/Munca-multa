import math
import random

class TournamentServices:
    def __init__(self, repository):
        """
        Initializes the service with a data repository.
        Loads the initial list of players into memory.
        """

        self._repository = repository
        self._active_players = self._repository.load_players()

    @property
    def get_active_players(self):
        return self._active_players

    def set_active_players(self, player_list):
        """
        Updates the list of players remaining in the tournament.
        """

        self._active_players = player_list

    def get_players_sorted_desc(self):
        """
        Returns players sorted by strength in descending order.
        Used for displaying the pre-tournament rankings.
        """
        return sorted(self._active_players, key=lambda x: x.get_strength, reverse=True)

    def get_players_sorted_asc(self):
        """
        Returns players sorted by strength in ascending order
        Used to determine who must play in the qualification round.
        """

        return sorted(self._active_players, key=lambda x: x.get_strength)

    def calculate_qualifier_needs(self):
        """
        Calculates if a qualification round is needed based on the power of 2 rule.
        """

        count = len(self._active_players)

        power_of_2 = 2 ** int(math.log2(count))

        if count == power_of_2:
            return (False, 0, 0)

        num_to_eliminate = count - power_of_2
        num_qualifiers = num_to_eliminate * 2

        return (True, num_qualifiers, num_to_eliminate)

    def generate_pairings(self, player_pool):
        """
        Takes a list of players, shuffles them, and creates pairs.
        """

        pool_copy = player_pool[:]
        random.shuffle(pool_copy)

        pairings = []

        for i in range(0, len(pool_copy), 2):
            if i + 1 < len(pool_copy):
                pairings.append((pool_copy[i], pool_copy[i+1]))
        return pairings

    def register_win(self, winner):
        """
        The winner's strength increases by 1 after a match.
        """

        current_strength = winner.get_strength()
        winner.get_strength = current_strength + 1
        return winner

    def get_round_name(self, num_players, is_qualifier=False):
        """
        Returns the display name for the current round based on player count.
        """

        if is_qualifier:
            return "Qualification Round"

        if num_players == 2:
            return "Final"
        elif num_players == 4:
            return "Semi-Finals"
        elif num_players == 8:
            return "Quarter-Finals"
        else:
            return f"Round of {num_players}"