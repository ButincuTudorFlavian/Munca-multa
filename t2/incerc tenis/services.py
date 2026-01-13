class Services:
    def __init__(self, repo):
        self.repo = repo

    def list_all_for_strenght_descending(self):
        all_players = self.repo.get_all()
        strenght_descending = sorted(all_players, key=lambda x: x.get_strenght(), reverse=True)
        return strenght_descending