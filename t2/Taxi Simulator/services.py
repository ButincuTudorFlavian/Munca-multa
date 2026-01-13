import random
from operator import truediv

from domain import Taxi

class TaxiService:
    """
    Contains the business logic for the Taxi Simulator.
    Handles coordinate generation, distance calculations, and ride assignments.
    """

    def __init__(self, repository):
        """
        Initializes the service with a repository instance.
        """
        self._repository = repository

    def _calculate_manhattan_distance(self, x1, y1, x2, y2):
        """
        Helper method to calculate the Manhattan distance between two points.
        Formula: |x1 - x2| + |y1 - y2|
        """
        return abs(x1 - x2) + abs(y1 - y2)

    def generate_initial_taxis(self,  count):
        """
        Generates 'count' number of taxis at random locations.
        Requirement: The distance between any two taxis must be > 5
        """

        generated_count = 0
        existing_taxis = []

        while generated_count < count:
            cx = random.randint(0, 100)
            cy = random.randint(0, 100)

            valid = True

            for t in existing_taxis:
                dist = self._calculate_manhattan_distance(cx, cy, t.get_x, t.get_y)
                if dist <= 5:
                    valid = False
                    break

            if valid:
                new_taxi = Taxi(generated_count+1, cx, cy)
                existing_taxis.append(new_taxi)
                self._repository.add_taxi(new_taxi)
                generated_count += 1

    def get_sorted_taxis(self):
        """
        Returns the list of taxis sorted by total fare in descending order.
        """
        taxis = self._repository.get_all_taxis()
        return sorted(taxis, key=lambda t: t.get_total_fare, reverse=True)

    def process_ride(self, start_x, start_y, end_x, end_y):
        """
        Assigns a ride to the closest taxi and updates its state.

        Logic:
        1. Find the taxi closest to (start_x, start_y).
        2. Calculate the distance of the ride (start -> end).
        3. Add that distance to the taxi's total fare.
        4. Move the taxi to the coordinates
        """

        taxis = self._repository.get_all_taxis()
        closest_taxi = None
        min_dist = float("inf")
        for t in taxis:
            dist_to_start = self._calculate_manhattan_distance(t.get_x, t.get_y, start_x, start_y)
            if dist_to_start < min_dist:
                min_dist = dist_to_start
                closest_taxi = t

        if closest_taxi:
            ride_distance = self._calculate_manhattan_distance(start_x, start_y, end_x, end_y)
            closest_taxi.add_fare(ride_distance)
            closest_taxi.update_location(end_x, end_y)

            return closest_taxi, ride_distance

        return None, 0

    def generate_random_ride_coordinates(self):
        """
        Generates valid random coordinates for a simulated ride.
        """

        while True:
            sx, sy = random.randint(0, 100), random.randint(0, 100)
            ex, ey = random.randint(0, 100), random.randint(0, 100)

            dist = self._calculate_manhattan_distance(sx, sy, ex, ey)

            if dist >= 10:
                return sx, sy, ex, ey