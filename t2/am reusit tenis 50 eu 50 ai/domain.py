class Player:
    def __init__(self, id_player, name, strength):
        self.id_player = id_player
        self.name = name
        self.strength = strength

    def get_id(self):
        return self.id_player

    def get_name(self):
        return self.name

    def get_strength(self):
        return self.strength

    def set_strength(self, new_strength):
        self.strength = new_strength

    def __str__(self):
        return f"{self.name} (ID: {self.id_player}) - Power: {self.strength}"

    def __repr__(self):
        return self.__str__()