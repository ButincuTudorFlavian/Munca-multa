from domain import TennisPlayer

class TennisPlayerMemRepo:
    def __init__(self):
        self._data = {}

    def list_all_players(self):
        return list(self._data.values())


class TextFileTennisPlayerRepo(TennisPlayerMemRepo):
    def __init__(self, filename="tennis.txt"):
        super().__init__()
        self._filename = filename
        self.__load_file()

    def delete_player(self, player_id):
        for player in self.list_all_players():
            if player.get_id == player_id:
                del self._data[player_id]
        # self.__save_file()

    def __load_file(self):
        try:
            fin = open(self._filename, "r")
        except FileNotFoundError:
            return

        self._data = {}
        for line in fin:
            line_ok = line.strip().split(", ")
            if len(line_ok) < 3:
                continue
            id = int(line_ok[0])
            name = line_ok[1]
            strength = int(line_ok[2])
            tennis_player = TennisPlayer(id, name, strength)
            self._data[id] = tennis_player

        fin.close()

    def __save_file(self):
        fout = open(self._filename, "w")
        for tennis_player in self._data.values():
            fout.write(f"{tennis_player.get_id}, {tennis_player.get_name}, {tennis_player.get_strength}\n")