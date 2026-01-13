class Bus:
    def __init__(self, bus_id, route_code, model, times_used):
        self._bus_id = bus_id
        self._route_code = route_code
        self._model = model
        self._times_used = times_used

    @property
    def get_bus_id(self):
        return self._bus_id

    @property
    def get_route_code(self):
        return self._route_code

    @property
    def get_model(self):
        return self._model

    @property
    def get_times_used(self):
        return self._times_used

    def __str__(self):
        return f"{self._bus_id}, {self._route_code}, {self._model}, {self._times_used}"


class BusRoute:
    def __init__(self, route_code, length):
        self._route_code = route_code
        self._length = length

    @property
    def get_route_code(self):
        return self._route_code

    @property
    def get_route_length(self):
        return self._length

    def __str__(self):
        return f"{self._route_code}, {self._length}"