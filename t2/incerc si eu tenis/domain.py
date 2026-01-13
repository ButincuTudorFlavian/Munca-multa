class Player:
    def __init__(self, id: int, name, strength: int):
        self._id = id
        self._name = name
        self._strength = strength

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def strength(self):
        return self._strength
