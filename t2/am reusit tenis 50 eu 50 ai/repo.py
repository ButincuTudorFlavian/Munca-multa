from domain import Player


class PlayerRepo:
    def __init__(self, filename):
        self.filename = filename
        self.player_list = []
        self.load_file()

    def load_file(self):
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()
                for line in lines:
                    line = line.strip()
                    if not line:
                        continue

                    parts = line.split(',')
                    if len(parts) < 3:
                        continue

                    id_player = parts[0].strip()
                    name = parts[1].strip()
                    try:
                        strength = int(parts[2].strip())
                        self.player_list.append(Player(id_player, name, strength))
                    except ValueError:
                        pass

        except FileNotFoundError:
            print("File not found")

    def get_all(self):
        return self.player_list