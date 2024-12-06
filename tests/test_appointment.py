import unittest
from models.appointment import Appointment

class TestAppointment(unittest.TestCase):

    def setUp(self):
        """Setup for each test."""
        # Create an Appointment instance with sample values
        self.appointment = Appointment("Invitee 1", "2024-12-06", 10, 11)

    def test_appointment_initialization(self):
        """Test the correct initialization of the Appointment object."""
        self.assertEqual(self.appointment.invitee_name, "Invitee 1")
        self.assertEqual(self.appointment.date, "2024-12-06")
        self.assertEqual(self.appointment.start_hour, 10)
        self.assertEqual(self.appointment.end_hour, 11)

    def test_appointment_str(self):
        """Test the string representation of the Appointment object."""
        expected_str = "Date: 2024-12-06, Time: 10:00 - 11:00, Invitee: Invitee 1"
        self.assertEqual(str(self.appointment), expected_str)

if __name__ == '__main__':
    unittest.main()
