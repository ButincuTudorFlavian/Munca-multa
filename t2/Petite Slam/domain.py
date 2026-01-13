class Player:
    """
    Represents a tennis player in the tournament.
    """

    def __init__(self, player_id, name, strength):
        self._player_id = player_id
        self._name = name
        self._strength = int(strength)

    @property
    def get_player_id(self):
        return self._player_id

    @property
    def get_name(self):
        return self._name

    @property
    def get_strength(self):
        return self._strength

    @get_strength.setter
    def get_strength(self, value):
        self._strength = value

    def __str__(self):
        return f"[ID: {self._player_id}] Name: {self._name}, Strength: {self._strength}"
