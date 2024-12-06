import unittest
from models.availability_rule import AvailabilityRule

class TestAvailabilityRule(unittest.TestCase):

    def test_initialization_with_defaults(self):
        """Test initialization with default availability values."""
        rule = AvailabilityRule()
        self.assertEqual(rule.start_hour, 10)
        self.assertEqual(rule.end_hour, 17)
        self.assertEqual(rule.days_of_week, {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"})

    def test_update_rule(self):
        """Test updating the availability rule."""
        rule = AvailabilityRule()
        rule.update_rule(9, 18, {"Monday", "Tuesday"})
        self.assertEqual(rule.start_hour, 9)
        self.assertEqual(rule.end_hour, 18)
        self.assertEqual(rule.days_of_week, {"Monday", "Tuesday"})

    def test_is_valid_slot_valid(self):
        """Test if a valid slot is recognized correctly."""
        rule = AvailabilityRule()
        valid_slot = rule.is_valid_slot("Monday", 10, 11)
        self.assertTrue(valid_slot)

    def test_is_valid_slot_invalid_day(self):
        """Test if an invalid day is recognized correctly."""
        rule = AvailabilityRule()
        invalid_day_slot = rule.is_valid_slot("Saturday", 10, 11)
        self.assertFalse(invalid_day_slot)

    def test_is_valid_slot_invalid_time(self):
        """Test if invalid time slots are recognized correctly."""
        rule = AvailabilityRule()
        invalid_time_slot = rule.is_valid_slot("Monday", 9, 11)
        self.assertFalse(invalid_time_slot)

    def test_is_valid_slot_boundary(self):
        """Test boundary condition where start and end hour are exactly within the availability."""
        rule = AvailabilityRule()
        valid_boundary_slot = rule.is_valid_slot("Monday", 10, 11)
        self.assertTrue(valid_boundary_slot)

    def test_invalid_end_time(self):
        """Test invalid scenario where start time is greater than end time."""
        rule = AvailabilityRule()
        with self.assertRaises(ValueError):
            rule.update_rule(17, 10, {"Monday"})

if __name__ == '__main__':
    unittest.main()
