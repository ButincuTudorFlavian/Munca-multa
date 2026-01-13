from services import AddressService, AddressError
from repository import AddressTextFileRepository

class UI:
    def __init__(self, address_service: AddressService):
        self._address_service = address_service
        self.running = True

    @staticmethod
    def print_menu():
        print(f"\nWelcome to the Taxi Company!")
        print("  1. List All Addresses")
        print("  2. Add Address")
        print("  3. Determine Taxi Positions")
        print("  4. Determine Optimal Taxi Position")
        print("  x. Exit")

    @staticmethod
    def run():
        try:
            address_repository = AddressTextFileRepository()
            address_service = AddressService(address_repository)
            return UI(address_service)
        except Exception as e:
            print(e)
            return None

    def user_run(self):
        if self._address_service is None:
            print("Address repository not initialized")
            return

        while self.running:
            self.print_menu()
            option = input("Enter your choice: ")
            if option == "1":
                try:
                    self.list_all_addresses()
                except Exception as e:
                    print(e)
            elif option == "2":
                try:
                    self.add_address()
                except Exception as e:
                    print(e)
            elif option == "3":
                try:
                    self.calculate_taxi()
                except Exception as e:
                    print(e)
            elif option == "4":
                try:
                    self.calculate_position()
                except Exception as e:
                    print(e)
            elif option == "x":
                self.running = False
            else:
                print("Invalid choice")

    def list_all_addresses(self):
        address_list = self._address_service.list_addresses()
        for address in address_list:
            print(address)

    def add_address(self):
        id = input("Enter Address ID: ")
        name = input("Enter address name: ")
        number = input("Enter address number: ")
        x_coordinate = input("Enter x coordinate: ")
        y_coordinate = input("Enter y coordinate: ")
        self._address_service.add_address(id, name, number, x_coordinate, y_coordinate)
        print("Address added successfully")

    def calculate_taxi(self):
        x = int(input("Enter x coordinate: "))
        y = int(input("Enter y coordinate: "))
        distance = int(input("Enter a distance: "))
        address_list = self._address_service.calculate_addresses(x, y, distance)
        print("Taxi positions calculated successfully: ")
        for address in address_list:
            print(address)

    def calculate_position(self):
        result_x, result_y = self._address_service.calculate_position()
        print(f"Taxi positions calculated successfully: {result_x}, {result_y}")

if __name__ == "__main__":
    ui = UI.run()
    if ui is not None:
        ui.user_run()