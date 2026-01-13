from domain import Bus, BusRoute

class BusMemoryRepo:
    def __init__(self, data):
        self._data = data

    def list_buses(self):
        return list(self._data.values())

class BusTextFIleRepo(BusMemoryRepo):
    def __init__(self, file_name="buses.txt"):
        super().__init__(self)
        self._file_name = file_name
        self.__load_file()

    def __load_file(self):
        try:
            fin = open(self._file_name, "r")
        except FileNotFoundError:
            return
        self._data = {}
        for line in fin:
            line_ok = line.strip().split(", ")
            if len(line_ok) < 4:
                continue
            bus_id = line_ok[0]
            route = line_ok[1]
            model = line_ok[2]
            times_used = line_ok[3]
            bus = Bus(bus_id, route, model, times_used)
            self._data[bus_id] = bus
        fin.close()


    def __save_file(self):
        fout = open(self._file_name, "w")
        for bus in self._data:
            fout.write(f"{bus.get_bus_id}, {bus.get_route}, {bus.get_model}, {bus.get_times_used}\n")
            fout.write("\n")

class BusRouteMemoryRepo:
    def __init__(self, data):
        self._data = data

    def list_routes(self):
        return list(self._data.values())

class BusRouteTextFIleRepo(BusRouteMemoryRepo):
    def __init__(self, file_name="bus_routes.txt"):
        super().__init__(self)
        self._file_name = file_name
        self.__load_file()

    def __load_file(self):
        try:
            fin = open(self._file_name, "r")
        except FileNotFoundError:
            return
        self._data = {}
        for line in fin:
            line_ok = line.strip().split(", ")
            if len(line_ok) < 2:
                continue
            route_code = line_ok[0]
            length = line_ok[1]
            route = BusRoute(route_code, length)
            self._data[route_code] = route
        fin.close()


    def __save_file(self):
        fout = open(self._file_name, "w")
        for route in self._data:
            fout.write(f"{route.get_route_code}, {route.get_route_length}\n")
            fout.write("\n")