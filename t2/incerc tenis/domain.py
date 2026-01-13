class Player:
    def __init__(self, id, name, strenght):
        self.__id = id
        self.__name = name
        self.__strenght = strenght

    def get_strenght(self):
        return self.__strenght

    def get_name(self):
        return self.__name

    def __str__(self):
        return f"{self.__name} (ID: {self.__id}) - Strenght: {self.__strenght}"