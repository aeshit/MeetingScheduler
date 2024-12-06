class Calendar:
    def __init__(self):
        """
        Initialize the Calendar.

        The calendar starts with an empty list of appointments.
        """
        self.appointments = []  # List of Appointment objects, initially empty.

    def add_appointment(self, appointment):
        """
        Add an appointment to the calendar.

        Args:
            appointment (Appointment): The appointment object to be added.
        """
        self.appointments.append(appointment)  # Add the provided appointment to the list
        print(f"Appointment added for {appointment.invitee_name} on {appointment.date} "
              f"from {appointment.start_hour}:00 to {appointment.end_hour}:00.")  # Print confirmation message

    def list_upcoming_appointments(self):
        """
        List all upcoming appointments.

        Returns:
            list: A list of all Appointment objects currently in the calendar.
        """
        return self.appointments  # Return the list of appointments, including past and future ones
