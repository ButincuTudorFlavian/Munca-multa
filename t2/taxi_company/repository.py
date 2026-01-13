from domain import Address

class AddressMemoRepository:
    def __init__(self):
        self._data = {}

    def list_all(self):
        return list(self._data.values())

    def add_address(self, id, name, number, x, y):
        self._data[id] = Address(id, name, number, x, y)

class AddressTextFileRepository(AddressMemoRepository):
    def __init__(self, filename="address.txt"):
        super().__init__()
        self._filename = filename
        self.__load_file()

    def add_address(self, id, name, number, x, y):
        self._data[id] = Address(id, name, number, x, y)
        self.__save_file()

    def __load_file(self):
        try:
            fin = open(self._filename, "r")
        except FileNotFoundError:
            return
        self._data = {}
        for line in fin:
            line_ok = line.strip().split(", ")
            if len(line_ok) < 5:
                continue
            id = line_ok[0]
            name = line_ok[1]
            number = line_ok[2]
            x_coord = line_ok[3]
            y_coord = line_ok[4]
            self._data[id] = Address(id, name, number, x_coord, y_coord)

        fin.close()

    def __save_file(self):
        fout = open(self._filename, "w")
        for address in self._data.values():
            fout.write(f"{address.get_id}, {address.get_name}, {address.get_number}, {address.get_x_coord}, {address.get_y_coord}\n")

        fout.close()