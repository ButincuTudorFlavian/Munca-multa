class ConsoleUI:
    """
    Handles the user interface for the Taxi Simulator
    """

    def __init__(self, services):
        """
        Initializes the UI with a reference to the service layer
        """
        self._services = services

    def display_taxis(self):
        """
        Prints out the list of taxis
        """
        taxis = self._services.get_sorted_taxis()
        for t in taxis:
            print(t)

    def run_init(self):
        while True:
            try:
                num_input = input("How many operational taxis do you want (1-10)?\n")
                num = int(num_input)

                if 1 <= num <= 10:
                    self._services.generate_initial_taxis(num)
                    break
                else:
                    print("Please enter a number between 1-10")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        self.display_taxis()

    def handle_manual_ride(self):
        """
        Allow the user to manually enter ride coordinates.
        """

        try:
            raw = input("Enter Start X, Start Y, End X, End Y:\n")
            parts = [int(p.strip()) for p in raw.replace(",", " ").split()]

            if len(parts) != 4:
                print("Error: Enter 4 separated numbers")
                return

            sx, sy, ex, ey = parts

            taxi, cost = self._services.process_ride(sx, sy, ex, ey)

            if taxi:
                print(f"Ride assigned to Taxi #{taxi.get_taxi_id}.")
                print(f"Ride Cost (Distance): {cost}")
                print(f"New Location: ({taxi.get_x}, {taxi.get_y})")
            else:
                print("Error: No taxis available.")
        except ValueError:
            print("Invalid input. Please ensure all coordinates are integers.")

    def handle_simulation(self):
        sx, sy, ex, ey = self._services.generate_random_ride_coordinates()
        print(f"Generated Ride: Start({sx}, {sy}) -> End({ex}, {ey})")

        taxi, cost = self._services.process_ride(sx, sy, ex, ey)

        if taxi:
            print(f"Ride assigned to Taxi #{taxi.get_taxi_id}.")
            print(f"Ride Cost: {cost}.")

    def start(self):
        print("Welcome to the Taxi Simulator!")
        self.run_init()

        while True:
            print("\nMAIN MENU:")
            print("1. Add a ride (Manual input)")
            print("2. Simulate a ride (Random generation)")
            print("0. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.handle_manual_ride()
                self.display_taxis()  # Requirement 4: Display situation after ride
            elif choice == "2":
                self.handle_simulation()
                self.display_taxis()  # Requirement 4: Display situation after ride
            elif choice == "0":
                print("Exiting application. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")