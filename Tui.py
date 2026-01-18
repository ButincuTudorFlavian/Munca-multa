
class UI:
    def __init__(self,service):
        self._service=service

    def _run(self):
        while True:
            self._menu()
            choice=int(input("Enter your choice:"))
            if choice==1:
                self._add_route()
            if choice==2:
                self._display_all_routes()
            if choice==3:
                self.buy_tickets()
            if choice==4:
                self._display_all_tickets()
            if choice==0:
                break

    def _menu(self):
        print("MENU")
        print("1.Add a route")
        print("2.Display all routes")
        print("3.Buy a ticket")
        print("4.Display all tickets")
        print("0.EXIT")

    def _add_route(self):
        departure_city=input("Enter departure city:")
        departure_time=input("Enter departure time:")
        arrival_city=input("Enter arrival city:")
        arrival_time=input("Enter arrival time:")
        tickets=int(input("Enter tickets:"))
        self._service.add_route(departure_city,departure_time,arrival_city,arrival_time,tickets)
        print("Route added!")

    def _display_all_routes(self):
        for route in self._service.display_all_routes():
            print(route)

    def buy_tickets(self):
        choice=input("Enter the number of the train:")

        for route in self._service.display_all_routes():
            if route.get_number()==choice:
                self._service.add_purchase(route.get_d_time(),route.get_a_time(),choice,0)
        print("ticket added")

    def _display_all_tickets(self):
        for ticket in self._service.display_all_tickets():
            print(ticket)