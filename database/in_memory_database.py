from models.calendar_owner import CalendarOwner

class InMemoryDatabase:
    """
    A singleton class that simulates an in-memory database for storing and managing CalendarOwners.

    This class is designed as a singleton, meaning only one instance of it can exist throughout the application.

    Attributes:
        _instance (InMemoryDatabase): The singleton instance of the InMemoryDatabase class.
        _data (dict): A dictionary holding all stored data. It contains a dictionary for calendar owners.
    """
    _instance = None  # This will hold the single instance of the class
    _data = {"calendar_owners": {}}  # Simulated in-memory data storage for calendar owners

    @staticmethod
    def get_instance():
        """
        Static method to get the singleton instance of InMemoryDatabase.

        Returns:
            InMemoryDatabase: The singleton instance of the InMemoryDatabase.
        """
        if InMemoryDatabase._instance is None:
            InMemoryDatabase._instance = InMemoryDatabase()  # Create the instance if it doesn't exist
        return InMemoryDatabase._instance

    def __init__(self):
        """
        Private constructor to prevent instantiation from outside the class.

        If an instance already exists, an exception is raised, ensuring that the class follows the singleton pattern.
        """
        if InMemoryDatabase._instance is not None:
            raise Exception("This class is a singleton!")  # Raise an error if an attempt is made to instantiate again
        InMemoryDatabase._instance = self  # Set the singleton instance

    def add_calendar_owner(self, calendar_owner_id: str, calendar_owner: "CalendarOwner"):
        """
        Adds a new CalendarOwner to the in-memory database.

        Args:
            calendar_owner_id (str): The unique identifier for the CalendarOwner.
            calendar_owner (CalendarOwner): The CalendarOwner object to add.
        """
        self._data["calendar_owners"][calendar_owner_id] = calendar_owner

    def get_calendar_owner(self, calendar_owner_id: str) -> "CalendarOwner":
        """
        Retrieves a CalendarOwner by its ID.

        Args:
            calendar_owner_id (str): The unique identifier for the CalendarOwner to fetch.

        Returns:
            CalendarOwner: The CalendarOwner associated with the provided ID, or None if not found.
        """
        return self._data["calendar_owners"].get(calendar_owner_id)  # Returns None if not found

    def list_calendar_owners(self):
        """
        Lists all the CalendarOwners stored in the in-memory database.

        Returns:
            list: A list of CalendarOwner objects stored in the database.
        """
        return self._data["calendar_owners"].values()  # Return all values (CalendarOwner objects)

    def log_data(self):
        """
        A debugging function that prints the stored data in the database.

        This is useful for logging and inspecting the current state of the database.
        """
        for owner_id, owner in self._data["calendar_owners"].items():
            print(f"CalendarOwnerID: {owner_id}, Name: {owner.name}")  # Print out each calendar owner's ID and name
