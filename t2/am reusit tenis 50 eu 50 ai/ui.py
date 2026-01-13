class Console:
    def __init__(self, service):
        self._service = service

    def play_matches(self, pairs, round_name):
        print(f"\n--- {round_name} ---")
        winners = []

        for p1, p2 in pairs:
            print(f"Match: {p1.get_name()} [{p1.get_strength()}]  VS  {p2.get_name()} [{p2.get_strength()}]")

            while True:
                opt = input(f"Winner (1 for {p1.get_name()} / 2 for {p2.get_name()}): ")
                if opt == "1":
                    print(f"-> Winner: {p1.get_name()}")
                    self._service.increase_strength(p1)
                    winners.append(p1)
                    break
                elif opt == "2":
                    print(f"-> Winner: {p2.get_name()}")
                    self._service.increase_strength(p2)
                    winners.append(p2)
                    break
                else:
                    print("Invalid option.")
        return winners

    def run_tournament(self):
        exempt_players, qual_pairs = self._service.prepare_qualification()

        qualified_winners = []
        if qual_pairs:
            qualified_winners = self.play_matches(qual_pairs, "QUALIFYING ROUND")

        active_players = exempt_players + qualified_winners

        while len(active_players) > 1:
            round_name = f"Last {len(active_players)}"
            if len(active_players) == 4:
                round_name = "SEMI-FINALS"
            if len(active_players) == 2:
                round_name = "FINAL"

            pairs = self._service.make_random_pairs(active_players)
            active_players = self.play_matches(pairs, round_name)

        winner = active_players[0]
        print(f"   CHAMPION: {winner.get_name()} (Final Power: {winner.get_strength()})")

    def run(self):
        while True:
            print("\n1. Display all players")
            print("2. START TOURNAMENT")
            print("x. Exit")

            cmd = input("Command: ")

            if cmd == "1":
                players = self._service.list_all_descending()
                for p in players:
                    print(p)
            elif cmd == "2":
                self.run_tournament()
            elif cmd == "x":
                break
            else:
                print("Invalid command.")