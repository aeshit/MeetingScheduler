import unittest
from models.appointment import Appointment
from models.invitee import Invitee
from models.calendar_owner import CalendarOwner

class TestCalendarOwner(unittest.TestCase):

    def test_add_invitee(self):
        """Test adding an invitee to the calendar owner's invitee list."""
        calendar_owner = CalendarOwner("1", "Owner 1")
        invitee = Invitee("Invitee 1", calendar_owner)
        
        # Add invitee and check the list of invitees
        calendar_owner.add_invitee(invitee)
        self.assertEqual(len(calendar_owner.invitees), 1)
        self.assertEqual(calendar_owner.invitees[0].name, "Invitee 1")

    def test_list_invitees(self):
        """Test listing invitees for a calendar owner."""
        calendar_owner = CalendarOwner("1", "Owner 1")
        invitee1 = Invitee("Invitee 1", calendar_owner)
        invitee2 = Invitee("Invitee 2", calendar_owner)
        
        calendar_owner.add_invitee(invitee1)
        calendar_owner.add_invitee(invitee2)

        invitees = calendar_owner.list_invitees()
        
        # Ensure both invitees are listed
        self.assertEqual(invitees, ["Invitee 1", "Invitee 2"])

    def test_setup_availability_valid(self):
        """Test setting up availability for a calendar owner with valid times."""
        calendar_owner = CalendarOwner("1", "Owner 1")
        calendar_owner.setup_availability("9 AM", "5 PM", {"Monday", "Tuesday"})
        
        # Check the updated availability
        availability = calendar_owner.get_availability()
        self.assertEqual(availability["start_hour"], 9)
        self.assertEqual(availability["end_hour"], 17)
        self.assertEqual(availability["days_of_week"], {"Monday", "Tuesday"})

    def test_setup_availability_invalid_time(self):
        """Test that setting up availability with an invalid time raises an error."""
        calendar_owner = CalendarOwner("1", "Owner 1")
        
        with self.assertRaises(ValueError):
            calendar_owner.setup_availability("5 PM", "3 PM", {"Monday"})

    def test_validate_slot_booking_valid(self):
        """Test validating a valid slot booking."""
        calendar_owner = CalendarOwner("1", "Owner 1")
        calendar_owner.setup_availability("9 AM", "5 PM", {"Monday", "Tuesday"})
        
        is_valid = calendar_owner.validate_slot_booking("Monday", "10 AM", "11 AM")
        self.assertTrue(is_valid)

    def test_validate_slot_booking_invalid(self):
        """Test validating an invalid slot booking."""
        calendar_owner = CalendarOwner("1", "Owner 1")
        calendar_owner.setup_availability("9 AM", "5 PM", {"Monday", "Tuesday"})
        
        is_valid = calendar_owner.validate_slot_booking("Monday", "8 AM", "9 AM")
        self.assertFalse(is_valid)

    def test_get_availability(self):
        """Test retrieving the current availability."""
        calendar_owner = CalendarOwner("1", "Owner 1")
        calendar_owner.setup_availability("10 AM", "4 PM", {"Monday", "Tuesday"})
        
        availability = calendar_owner.get_availability()
        self.assertEqual(availability["start_hour"], 10)
        self.assertEqual(availability["end_hour"], 16)
        self.assertEqual(availability["days_of_week"], {"Monday", "Tuesday"})

    def test_list_appointments_empty(self):
        """Test listing appointments when no appointments are added."""
        calendar_owner = CalendarOwner("1", "Owner 1")
        appointments = calendar_owner.list_appointments()
        
        # Since no appointments are added, the list should be empty
        self.assertEqual(appointments, [])

    def test_list_appointments_non_empty(self):
        """Test listing appointments when appointments are present."""
        calendar_owner = CalendarOwner("1", "Owner 1")
        invitee = Invitee("Invitee 1", calendar_owner)
        appointment = Appointment("Invitee 1", "2024-12-06", 10, 11)
        
        # Add appointment
        calendar_owner.calendar.add_appointment(appointment)
        appointments = calendar_owner.list_appointments()

        # Check if the appointment is listed
        self.assertEqual(len(appointments), 1)
        self.assertEqual(appointments[0].invitee_name, "Invitee 1")
        self.assertEqual(appointments[0].date, "2024-12-06")
        self.assertEqual(appointments[0].start_hour, 10)
        self.assertEqual(appointments[0].end_hour, 11)

if __name__ == '__main__':
    unittest.main()
