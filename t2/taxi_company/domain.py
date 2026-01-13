class Address:
    def __init__(self, id, name, number, x_coord, y_coord):
        self._id = id
        self._name = name
        self._number = number
        self._x_coord = x_coord
        self._y_coord = y_coord

    @property
    def get_id(self):
        return self._id

    @property
    def get_name(self):
        return self._name

    @property
    def get_number(self):
        return self._number

    @property
    def get_x_coord(self):
        return self._x_coord

    @property
    def get_y_coord(self):
        return self._y_coord

    def __str__(self):
        return f"{self._id}, {self._name}, {self._number}, {self.get_x_coord}, {self.get_y_coord}"
