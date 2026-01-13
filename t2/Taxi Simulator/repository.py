from domain import Taxi

class TaxiRepository:
    """
    Manages the storage of Taxi objects in memory.
    """

    def __init__(self):
        """
        Initializes the repository with an empty list of taxis.
        """
        self._taxis = []

    def add_taxi(self, taxi):
        """
        Adds a new Taxi object to the repository.
        """
        self._taxis.append(taxi)

    def get_all_taxis(self):
        """
        Retrieves the list of all currently operational taxis.
        """
        return self._taxis