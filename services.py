import math
import random

class AddressError(Exception):
    pass

class AddressService:
    def __init__(self, address_repo):
        self._address_repo = address_repo

    @staticmethod
    def generate_id():
        return random.randint(1, 999)

    def address_ok(self, id, name, number, x, y):
        try:
            id = int(id)
            number = int(number)
            x = int(x)
            y = int(y)
        except AddressError:
            raise AddressError("Address is not valid")

        for address in self._address_repo.list_all():
            if address.get_id == id:
                return False
        if len(name) < 3:
            return False
        if number < 0 or number > 100:
            return False
        if x < -100 or x > 100:
            return False
        if y < -100 or y > 100:
            return False
        return True

    def list_addresses(self):
        return self._address_repo.list_all()

    def add_address(self, id, name, number, x, y):
        if self.address_ok(id, name, number, x, y):
            self._address_repo.add_address(id, name, number, x, y)
        else:
            raise AddressError("Invalid address")

    @staticmethod
    def calculate_distance_x_y(x, y, x1, y1):
        return math.sqrt((x - int(x1)) ** 2 + (y - int(y1)) ** 2)

    def calculate_addresses(self, x, y, distance):
        list_ok = []
        for address in self._address_repo.list_all():
            dist = math.sqrt((x - int(address.get_x_coord)) ** 2 + (y - int(address.get_y_coord)) ** 2)
            if dist <= distance:
                list_ok.append(address)
        return list_ok

    def verif(self, x, y):
        for address in self._address_repo.list_all():
            if address.get_x_coord == x and address.get_y_coord == y:
                return False
        return True

    def calculate_position(self):
        sum_min = 100000000
        x_min , y_min = 0, 0
        for x in range(-100, 100):
            for y in range(-100, 100):
                if self.verif(x, y):
                    sum = 0
                    for address in self._address_repo.list_all():
                        sum += self.calculate_distance_x_y(x, y, address.get_x_coord, address.get_y_coord)
                    if sum < sum_min:
                        sum_min = sum
                        x_min = x
                        y_min = y

        return x_min, y_min
