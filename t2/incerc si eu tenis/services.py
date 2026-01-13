class GameService:
    def __init__(self, repo):
        self._repo = repo

    def list_players(self):
        return self._repo.get_players()



    def main_game(self):

