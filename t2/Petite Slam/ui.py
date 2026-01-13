class ConsoleUI:
    """
    Handles all user interaction (Console Input/Output).
    Strictly separated from logic and data access.
    """

    def __init__(self, service):
        """
        Inject the service layer to access adding logic
        """

        self._service = service

    def _play_single_match(self, p1, p2):
        """
        Helper method to manage the interaction for a single match.
        """
        print(f"\nMatch: {p1.get_name} (Str: {p1.get_strength}) vs {p2.get_name} (Str: {p2.get_strength})")

        winner = None
        while winner is None:
            try:
                choice = int(input(f"Choose who won (1/2)"))
                if choice == 1:
                    winner = p1
                elif choice == 2:
                    winner = p2
                else:
                    print("Invalid choice. Please enter 1 or 2")
            except ValueError:
                print("Invalid choice. Please enter a number")

            self._service.register_win(winner)
            print(f"Winner: {winner.get_name}! New Strength: {winner.get_strength}")
            return winner

    def display_rankings(self):
        """
        Sort the data from service and prints it
        """

        players = self._service.get_players_sorted_desc()
        for p in players:
            print(p)

    def run_qualifier(self):
        pass

    def run_main_rounds(self):
        """
        Main loop for the tournament until one player remains.
        """
        while len(self._service.get_active_players) > 1:
            current_players = self._service.get_active_players
            round_name = self._service.get_round_name(len(current_players))

            print(f"\n*** {round_name} ***")

            pairings = self._service.generate_pairings(current_players)
            next_round_players = []

            for p1, p2 in pairings:
                winner = self._play_single_match(p1, p2)
                next_round_players.append(winner)

            self._service.set_active_players(next_round_players)

        if self._service.get_active_players:
            winner = self._service.get_active_players[0]
            print(f"\n=== TOURNAMENT WINNER: {winner.get_name} ===")

    def start(self):
        if not self._service.get_active_players:
            print("No players found.")
            return

        self.display_rankings()
        self.run_qualifier()
        self.run_main_rounds()
