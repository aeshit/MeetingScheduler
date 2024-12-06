class AvailabilityRule:
    """
    A class to define and manage availability rules for specific days and time slots.
    """

    def __init__(self, start_hour: int = 10, end_hour: int = 17, days_of_week=None):
        """
        Initialize an AvailabilityRule object.

        :param start_hour: Start hour in 24-hour format, default is 10.
        :param end_hour: End hour in 24-hour format, default is 17.
        :param days_of_week: A set of days on which the rule applies, defaults to weekdays.
        """
        if days_of_week is None:
            days_of_week = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.days_of_week = days_of_week

    def update_rule(self, start_hour: int, end_hour: int, days_of_week: set):
        """
        Update the availability rule with new time and days.

        :param start_hour: New start hour in 24-hour format.
        :param end_hour: New end hour in 24-hour format.
        :param days_of_week: A new set of days on which the rule applies.
        :raises ValueError: If the start_hour is greater than or equal to end_hour.
        """
        # Validate time slot
        if start_hour >= end_hour:
            print(f"Invalid slot: {start_hour}:00 - {end_hour}:00")
            raise ValueError("Start hour must be less than end hour.")

        # Update rule properties
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.days_of_week = days_of_week
        print(f"Updated availability: {start_hour}:00 - {end_hour}:00 on {days_of_week}")

    def is_valid_slot(self, day: str, start_hour: int, end_hour: int) -> bool:
        """
        Check if a given time slot is valid based on the availability rule.

        :param day: The day of the week for the slot (e.g., "Monday").
        :param start_hour: Start hour in 24-hour format.
        :param end_hour: End hour in 24-hour format.
        :return: True if the slot is valid, otherwise False.
        """
        # Ensure the availability rule itself is valid
        if self.start_hour >= self.end_hour:
            return False

        # Check if the day and hours fall within the rule's constraints
        return (
            day in self.days_of_week
            and self.start_hour <= start_hour
            and self.end_hour >= end_hour
        )
