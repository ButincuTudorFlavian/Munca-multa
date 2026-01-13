from domain import Player

class MemoryRepo:
    def __init__(self):
        self._data = []

class FileRepo(MemoryRepo):
    def __init__(self, file_name):
        super().__init__()
        self._file_name = file_name
        self._load_file()

    def _load_file(self):
        with open(self._file_name) as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split('|')
                try:
                    id = int(parts[0])
                    strength = int(parts[2])
                except ValueError:
                    continue

                if len(parts) == 3:
                    abc = Player(id, parts[1], strength)
                    self._data.append(abc)

    def get_all_by_id(self):
        return self._data