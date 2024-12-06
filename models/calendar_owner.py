from models.calendar import Calendar  # For managing the owner's calendar
from models.invitee import Invitee  # To link invitees to the calendar owner
from models.availability_rule import AvailabilityRule  # For defining availability rules
from utils.utils import convert_to_24_hour, generate_uuid  # Utility functions for time conversion and ID generation


class CalendarOwner:
    def __init__(self, name: str, availability_rule: AvailabilityRule, ownerId: str = generate_uuid()):
        """Initialize a CalendarOwner with a name, availability rule, and optional unique ID."""
        self.id = ownerId  # Unique identifier for the calendar owner
        self.name = name  # Name of the calendar owner
        self.calendar = Calendar()  # Associated calendar object for managing appointments
        self.invitees = []  # List of invitees linked to this calendar owner
        self.availability_rule = availability_rule  # Availability rules for this calendar owner

    def __str__(self):
        """Return a string representation of the calendar owner."""
        return f"CalendarOwner(ID: {self.id}, Name: {self.name})"

    def add_invitee(self, invitee: Invitee):
        """
        Add an invitee to this calendar owner.

        Args:
            invitee (Invitee): The invitee to be added.
        """
        self.invitees.append(invitee)
        print(f"Invitee {invitee.name} added for CalendarOwner {self.name}.")

    def list_invitees(self):
        """
        List all invitees linked to this calendar owner.

        Returns:
            list: Names of all invitees.
        """
        return [invitee.name for invitee in self.invitees]
    
    def setup_availability(self, start_time: str, end_time: str, days_of_week: set):
        """
        Set up the availability rules for this calendar owner.

        Args:
            start_time (str): The start time of availability (e.g., "9 AM").
            end_time (str): The end time of availability (e.g., "5 PM").
            days_of_week (set): Days of the week the owner is available (e.g., {"Monday", "Tuesday"}).
        """
        start_hour = convert_to_24_hour(start_time)  # Convert start time to 24-hour format
        end_hour = convert_to_24_hour(end_time)  # Convert end time to 24-hour format

        # Validate that the start time is earlier than the end time
        if start_hour >= end_hour:
            raise ValueError(f"Invalid availability: start time {start_time} must be earlier than end time {end_time}.")

        # Update the availability rule
        self.availability_rule.update_rule(start_hour, end_hour, days_of_week)

    def validate_slot_booking(self, day: str, start_time: str, end_time: str) -> bool:
        """
        Validate if a booking falls within the availability rules.

        Args:
            day (str): Day of the week for the booking (e.g., "Monday").
            start_time (str): Start time of the booking (e.g., "10 AM").
            end_time (str): End time of the booking (e.g., "11 AM").

        Returns:
            bool: True if the booking is valid; False otherwise.
        """
        start_hour = convert_to_24_hour(start_time)  # Convert start time to 24-hour format
        end_hour = convert_to_24_hour(end_time)  # Convert end time to 24-hour format

        return self.availability_rule.is_valid_slot(day, start_hour, end_hour)

    def get_availability(self):
        """
        Retrieve the current availability rules.

        Returns:
            dict: Current availability rules including start hour, end hour, and days of the week.
        """
        return {
            "start_hour": self.availability_rule.start_hour,
            "end_hour": self.availability_rule.end_hour,
            "days_of_week": self.availability_rule.days_of_week
        }
    
    def list_appointments(self):
        """
        List all upcoming appointments for this calendar owner.

        Returns:
            list: List of upcoming appointments, or an empty list if no appointments are available.
        """
        print(f"\nUpcoming Appointments for {self.name}:")
        appointments = self.calendar.list_upcoming_appointments()  # Get upcoming appointments from the calendar
        if not appointments:
            print("No upcoming appointments.")
            return []  # Return an empty list when no appointments
        return appointments  # Return the list of appointments
