from repository import BusTextFIleRepo, BusRouteTextFIleRepo
from services import BusService, BusRouteService

class UI:
    def __init__(self, bus_service:BusService, route_service:BusRouteService):
        self._bus_service = bus_service
        self._route_service = route_service
        self.running = True

    @staticmethod
    def run():
        try:
            bus_repo = BusTextFIleRepo()
            route_repo = BusRouteTextFIleRepo()
            bus_service = BusService(bus_repo)
            route_service = BusRouteService(route_repo)
            return UI(bus_service, route_service)
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def print_menu():
        print("Welcome to Bus Tycoon")
        print("  1. List all buses")
        print("  2. List all routes")
        print("  3. List all buses on a specific route")
        print("  4. Calculate bus kilometers based on bus's id")
        print("  5. Display routes based on mileage")
        print("  x. Exit")

    def user_run(self):
        if self._bus_service is None or self._route_service is None:
            print("Bus/Route service was not initialized")
            return

        while self.running:
            self.print_menu()
            option = input("Enter your choice: ")
            if option == "1":
                self.list_buses()
            elif option == "2":
                self.list_routes()
            elif option == "3":
                self.list_buses_on_route()
            elif option == "4":
                self.calculate_km()
            elif option == "5":
                self.display_routes_on_mileage()
            else:
                self.running = False

    def list_buses(self):
        print("List of all buses: ")
        bus_list = self._bus_service.list_buses()
        for bus in bus_list:
            print(bus)
        print("\n")

    def list_routes(self):
        print("List of all routes: ")
        route_list = self._route_service.list_routes()
        for route in route_list:
            print(route)

    def list_buses_on_route(self):
        route = input("Enter a route code: ")
        bus_list = self._bus_service.list_bus_info_on_route(route)
        for bus in bus_list:
            print(bus)

    def calculate_km(self):
        bus_id = input("Enter a bus id: ")
        times, route_code = self._bus_service.bus_times(bus_id)
        km = self._route_service.route_km(route_code)
        times = int(times)
        km = int(km)
        calculate = times * km
        bus_info = self._bus_service.bus_info(bus_id)
        print("Bus kilometers: ", calculate)
        print("Bus data: ", bus_info)

    def display_routes_on_mileage(self):
        frequency = self._bus_service.calculate_times_on_one_route()
        ordered_routes = self._route_service.ordered_routes(frequency)
        print("Routes ordered by mileage: ", ordered_routes)
        """for route in ordered_routes:
            print(f"Route: {route} --> {str(ordered_routes[route])} km")"""

if __name__ == "__main__":
    ui = UI.run()
    if ui is not None:
        ui.user_run()
