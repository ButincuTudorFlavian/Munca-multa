from domain import Bus

class BusService:
    def __init__(self, bus_repo):
        self._bus_repo = bus_repo

    def list_buses(self):
        return self._bus_repo.list_buses()

    def list_bus_info_on_route(self, route_code):
        buses = []
        for bus in self._bus_repo.list_buses():
            if bus.get_route_code == route_code:
                buses.append(bus)
        return buses

    def bus_info(self, bus_id)->Bus:
        """
        Returns a bus object with all its information
        based on its given bus id
        :param bus_id: bus id
        :return: Bus object
        """
        info_bus = 0
        for bus in self._bus_repo.list_buses():
            if bus.get_bus_id == bus_id:
                info_bus = Bus(bus.get_bus_id, bus.get_route_code, bus.get_model, bus.get_times_used)
        return info_bus

    def bus_times(self, bus_id):
        """
        Returns how many times a bus was used on a route and that route's code
        based on a given bus id
        :param bus_id: bus id
        :return: times used, route's code
        """
        times = 0
        route = 0
        for bus in self._bus_repo.list_buses():
            if bus.get_bus_id == bus_id:
                times = bus.get_times_used
                route = bus.get_route_code
        return times, route

    def calculate_times_on_one_route(self):
        frequency = {}
        for bus in self._bus_repo.list_buses():
            if bus.get_route_code not in frequency:
                frequency[bus.get_route_code] = int(bus.get_times_used)
            else:
                frequency[bus.get_route_code] += int(bus.get_times_used)
        return frequency

class BusRouteService:
    def __init__(self, route_repo):
        self._route_repo = route_repo

    def list_routes(self):
        return self._route_repo.list_routes()

    def route_km(self, route_code):
        """
        Returns how many kms does a route have based on
        its given route code
        :param route_code: route code
        :return: number of kms
        """
        km = 0
        for route in self._route_repo.list_routes():
            if route.get_route_code == route_code:
                km = route.get_route_length
        return km

    def ordered_routes(self, frequency):
        for route in self._route_repo.list_routes():
            if route.get_route_code not in frequency:
                frequency[route.get_route_code] = 0
        calc_route = {}
        for route_id in frequency:
            km = self.route_km(route_id)
            calc_route[route_id] = int( int(km) * int(frequency[route_id]))
        sort_calc = sorted(calc_route.items(), key=lambda x: x[1], reverse=True)
        return sort_calc