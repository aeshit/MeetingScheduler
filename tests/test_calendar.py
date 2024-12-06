import unittest
from models.appointment import Appointment
from models.calendar import Calendar

class TestCalendar(unittest.TestCase):

    def test_add_appointment(self):
        """Test adding an appointment to the calendar."""
        calendar = Calendar()
        appointment = Appointment("Invitee 1", "2024-12-06", 10, 11)
        calendar.add_appointment(appointment)

        # Assert that the appointment was added correctly
        self.assertEqual(len(calendar.appointments), 1)
        self.assertEqual(calendar.appointments[0].invitee_name, "Invitee 1")
        self.assertEqual(calendar.appointments[0].date, "2024-12-06")
        self.assertEqual(calendar.appointments[0].start_hour, 10)
        self.assertEqual(calendar.appointments[0].end_hour, 11)

    def test_list_upcoming_appointments_empty(self):
        """Test listing upcoming appointments when no appointments are present."""
        calendar = Calendar()
        appointments = calendar.list_upcoming_appointments()

        # Assert that no appointments are listed
        self.assertEqual(appointments, [])

    def test_list_upcoming_appointments_non_empty(self):
        """Test listing upcoming appointments when appointments are present."""
        calendar = Calendar()
        appointment1 = Appointment("Invitee 1", "2024-12-06", 10, 11)
        appointment2 = Appointment("Invitee 2", "2024-12-07", 14, 15)
        calendar.add_appointment(appointment1)
        calendar.add_appointment(appointment2)

        appointments = calendar.list_upcoming_appointments()

        # Assert that the list contains both appointments
        self.assertEqual(len(appointments), 2)
        self.assertEqual(appointments[0].invitee_name, "Invitee 1")
        self.assertEqual(appointments[1].invitee_name, "Invitee 2")

if __name__ == '__main__':
    unittest.main()
