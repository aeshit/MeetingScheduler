import unittest
from models.appointment import Appointment
from models.invitee import Invitee
from models.calendar_owner import CalendarOwner
from utils.utils import convert_to_24_hour

class TestInvitee(unittest.TestCase):

    def setUp(self):
        """Setup for each test."""
        self.calendar_owner = CalendarOwner("1", "Owner 1")
        self.invitee = Invitee("Invitee 1", self.calendar_owner)
        # Set up a default availability for the calendar owner
        self.calendar_owner.setup_availability("9 AM", "5 PM", {"Monday", "Tuesday"})
        
    def test_search_available_slots(self):
        """Test searching for available slots."""
        available_slots = self.invitee.search_available_slots()
        expected_slots = [
            "Monday 9:00 - 10:00", "Monday 10:00 - 11:00", "Monday 11:00 - 12:00",
            "Monday 12:00 - 1:00", "Monday 1:00 - 2:00", "Monday 2:00 - 3:00",
            "Monday 3:00 - 4:00", "Monday 4:00 - 5:00",
            "Tuesday 9:00 - 10:00", "Tuesday 10:00 - 11:00", "Tuesday 11:00 - 12:00",
            "Tuesday 12:00 - 1:00", "Tuesday 1:00 - 2:00", "Tuesday 2:00 - 3:00",
            "Tuesday 3:00 - 4:00", "Tuesday 4:00 - 5:00"
        ]
        self.assertEqual(available_slots, expected_slots)

    def test_book_slot_valid(self):
        """Test booking a valid slot."""
        result = self.invitee.book_slot("Monday", "10 AM", "11 AM", "Monday")
        self.assertEqual(result, "Successfully booked slot: Monday 10 AM - 11 AM.")

if __name__ == '__main__':
    unittest.main()
