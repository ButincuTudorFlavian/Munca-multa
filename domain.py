class TennisPlayer:
    def __init__(self, id, name, strength):
        self._id = id
        self._name = name
        self._strength = strength

    @property
    def get_id(self):
        return self._id

    @property
    def get_name(self):
        return self._name

    @property
    def get_strength(self):
        return self._strength

    @get_strength.setter
    def set_strength(self, value):
        self._strength = value

    def __str__(self):
        return f"{self.get_id}, {self.get_name}, {self.get_strength}"