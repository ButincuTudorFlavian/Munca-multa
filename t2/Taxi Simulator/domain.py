class Taxi:
    def __init__(self, taxi_id, x, y):
        """
        Represents a taxi entity in the simulation system.
        """
        self._taxi_id = taxi_id
        self._x = x
        self._y = y
        self._total_fare = 0

    @property
    def get_taxi_id(self):
        """Returns the unique identifier of the taxi."""
        return self._taxi_id

    @property
    def get_x(self):
        """
        Returns the current X coordinate.
        """
        return self._x

    @property
    def get_y(self):
        """
        Returns the current Y coordinate.
        """
        return self._y

    @property
    def get_total_fare(self):
        """Returns the total fare accumulated by the taxi."""
        return self._total_fare

    def update_location(self, new_x, new_y):
        """
        Updates the taxi's current location to the new coordinates.
        Used when the taxi completes a ride.
        """
        self._x = new_x
        self._y = new_y

    def add_fare(self, amount):
        """
        Increases the total fare by the specified amount (distance).
        """
        self._total_fare = self._total_fare + amount

    def __str__(self):
        """
        Returns a string representation of the taxi for display purposes.
        """
        return f"Taxi #{self._taxi_id} | Loc: ({self._x},{self._y}) | Fare: {self._total_fare}"
