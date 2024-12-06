class Appointment:
    def __init__(self, invitee_name: str, date: str, start_hour: int, end_hour: int):
        """
        Initialize an Appointment.

        Args:
            invitee_name (str): The name of the invitee.
            date (str): The date of the appointment in YYYY-MM-DD format.
            start_hour (int): The starting hour of the appointment (24-hour format).
            end_hour (int): The ending hour of the appointment (24-hour format).
        """
        self.invitee_name = invitee_name  # Name of the person who booked the appointment
        self.date = date  # Appointment date in the format YYYY-MM-DD
        self.start_hour = start_hour  # Start time in 24-hour format (e.g., 10 for 10 AM)
        self.end_hour = end_hour  # End time in 24-hour format (e.g., 11 for 11 AM)

    def __str__(self):
        """
        String representation of the appointment.

        Returns:
            str: Formatted string with appointment details.
        """
        return f"Date: {self.date}, Time: {self.start_hour}:00 - {self.end_hour}:00, Invitee: {self.invitee_name}"
