import random


class Services:
    def __init__(self, repo):
        self.repo = repo

    def list_all_descending(self):
        return sorted(self.repo.get_all(), key=lambda x: x.get_strength(), reverse=True)

    def is_power_of_two(self, n):
        return (n > 0) and ((n & (n - 1)) == 0)

    def prepare_qualification(self):
        all_players = sorted(self.repo.get_all(), key=lambda x: x.get_strength())
        n = len(all_players)

        if self.is_power_of_two(n):
            return all_players, []
        k = 1
        while k * 2 < n:
            k = k * 2
        to_eliminate = n - k
        num_qualifiers = to_eliminate * 2

        weakest = all_players[:num_qualifiers]
        exempt = all_players[num_qualifiers:]

        random.shuffle(weakest)
        pairs = []
        for i in range(0, len(weakest) - 1, 2):
            pairs.append((weakest[i], weakest[i + 1]))

        return exempt, pairs

    def make_random_pairs(self, players):
        active = players[:]
        random.shuffle(active)
        pairs = []
        for i in range(0, len(active) - 1, 2):
            pairs.append((active[i], active[i + 1]))
        return pairs

    def increase_strength(self, player):
        player.set_strength(player.get_strength() + 1)