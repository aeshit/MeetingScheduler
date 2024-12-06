from datetime import datetime
import uuid

def convert_to_24_hour(time_str: str) -> int:
    """Convert time from 12-hour format (AM/PM) or 24-hour format to 24-hour format."""
    try:
        # Check if time is in 12-hour format with AM/PM (e.g., 9 AM or 4 PM)
        if 'AM' in time_str or 'PM' in time_str:
            time_obj = datetime.strptime(time_str, '%I %p')  # %I for 12-hour format with AM/PM
            return time_obj.hour  # Return the hour in 24-hour format
        else:
            # For 24-hour format, it's just a number representing the hour (e.g., 14, 9)
            time_obj = datetime.strptime(time_str, '%H')  # %H for 24-hour format (no minutes)
            return time_obj.hour  # Return the hour in 24-hour format
    except ValueError:
        raise ValueError(f"Invalid time format: {time_str}. Expected format 'HH AM/PM' or 'HH'.")


def generate_uuid():
  """Randomly generated hex string"""
  uuid_str = str(uuid.uuid4())
  return uuid_str