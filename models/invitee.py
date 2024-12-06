from models.appointment import Appointment
from utils.utils import convert_to_24_hour
from datetime import datetime, timedelta

class Invitee:
    def __init__(self, name, calendar_owner):
        """
        Initialize the Invitee.

        Args:
            name (str): The name of the invitee.
            calendar_owner (CalendarOwner): The calendar owner that the invitee is linked to.
        """
        self.name = name  # The name of the invitee
        self.calendar_owner = calendar_owner  # Link the invitee to a calendar owner
    
    def search_available_slots(self):
        """
        Search for available slots in the linked calendar owner's calendar.

        Loops through each day of the week and checks available time slots within the calendar owner's availability.

        Returns:
            list: A list of available time slots in string format (e.g., '2024-12-09 Monday Time: 9:00 - 10:00').
        """
        available_slots = []  # Initialize an empty list to hold available slots
        
        # Loop through all days in availability and check available time slots
        for day_name in self.calendar_owner.availability_rule.days_of_week:
            current_date = datetime.today()  # Get the current date
            
            # Map weekdays to corresponding integer values (Monday = 0, Tuesday = 1, etc.)
            weekday_map = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
            day_of_week = weekday_map[day_name]
            
            # Calculate the number of days ahead to reach the next occurrence of the given day
            days_ahead = (day_of_week - current_date.weekday()) % 7
            target_date = current_date + timedelta(days=days_ahead)  # Calculate the target date
            
            # Format the target date as YYYY-MM-DD
            day_str = target_date.strftime('%Y-%m-%d')
            
            # Loop through available hours for that day
            for hour in range(self.calendar_owner.availability_rule.start_hour, self.calendar_owner.availability_rule.end_hour):
                # Assume the slot is available until proven otherwise
                is_available = True
                
                # Check if there is any existing appointment for that date and hour
                for appointment in self.calendar_owner.calendar.appointments:
                    if (appointment.date == day_str and appointment.start_hour == hour):
                        is_available = False  # Slot is already booked
                        break
                
                # Check if the slot is within the owner's availability
                if not self._is_within_availability(hour, hour+1, day_name):
                    is_available = False  # Slot is outside of available hours

                if is_available:
                    available_slots.append(f"{day_str} {day_name} Time: {hour}:00 - {hour+1}:00")  # Add the available slot to the list

        return available_slots  # Return the list of available slots

    def book_slot(self, date: str, start_time: str, end_time: str, day: str): 
        """
        Book a slot for the invitee in the linked calendar owner's calendar.

        Args:
            date (str): The date to book the slot (format: 'YYYY-MM-DD').
            start_time (str): The start time in 12-hour format (e.g., '9 AM').
            end_time (str): The end time in 12-hour format (e.g., '10 AM').
            day (str): The day of the week (e.g., 'Monday').

        Returns:
            str: Confirmation message about the booking attempt (success or failure).
        """
        try:
            start_hour = convert_to_24_hour(start_time)  # Convert start time to 24-hour format
            end_hour = convert_to_24_hour(end_time)  # Convert end time to 24-hour format
        except ValueError as e:
            print(f"Invalid time format: {start_time}. {str(e)}")
        
        # Ensure the slot duration is valid (1-hour slots only)
        if end_hour - start_hour != 1:
            print(f"Invalid slot duration: {start_time} - {end_time}. Slots must be 1 hour.")
            raise ValueError("Invalid slot duration.")
        
        # Check for duplicate or overlapping bookings
        for appointment in self.calendar_owner.calendar.appointments:
            if appointment.date == date and appointment.start_hour == start_hour:
                return f"Slot already booked for {date} {start_time} - {end_time}."  # Return if slot is already booked

        # Ensure that the booking is within the calendar owner's available hours
        if not self._is_within_availability(start_hour, end_hour, day):
            return f"Invalid availability: The owner is unavailable at this time."  # Return if outside of available hours

        # If the slot is available, add the appointment
        self.calendar_owner.calendar.add_appointment(Appointment(self.name, date, start_hour, end_hour))
        return f"Successfully booked slot: {date} {start_time} - {end_time}."  # Return success message

    def _is_within_availability(self, start_hour, end_hour, day):
        """
        Check if the booking is within the available hours of the calendar owner.

        Args:
            start_hour (int): The start hour of the booking in 24-hour format.
            end_hour (int): The end hour of the booking in 24-hour format.
            day (str): The day of the week (e.g., 'Monday').

        Returns:
            bool: True if the booking is within the available hours, False otherwise.
        """
        # Check if the start and end hours are within the owner's availability
        return self.calendar_owner.availability_rule.start_hour <= start_hour < self.calendar_owner.availability_rule.end_hour and \
               self.calendar_owner.availability_rule.start_hour < end_hour <= self.calendar_owner.availability_rule.end_hour and \
               day in self.calendar_owner.availability_rule.days_of_week
