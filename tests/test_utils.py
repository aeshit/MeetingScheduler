import pytest
from utils.utils import convert_to_24_hour


def test_convert_to_24_hour_12_hour_format_am():
    """Test converting 12-hour format with AM to 24-hour format."""
    assert convert_to_24_hour("9 AM") == 9
    assert convert_to_24_hour("12 AM") == 0  # Midnight
    assert convert_to_24_hour("11 AM") == 11


def test_convert_to_24_hour_12_hour_format_pm():
    """Test converting 12-hour format with PM to 24-hour format."""
    assert convert_to_24_hour("1 PM") == 13
    assert convert_to_24_hour("12 PM") == 12  # Noon
    assert convert_to_24_hour("5 PM") == 17
    assert convert_to_24_hour("11 PM") == 23


def test_convert_to_24_hour_24_hour_format():
    """Test converting 24-hour format to 24-hour format."""
    assert convert_to_24_hour("00") == 0  # Midnight
    assert convert_to_24_hour("9") == 9
    assert convert_to_24_hour("13") == 13
    assert convert_to_24_hour("23") == 23


def test_convert_to_24_hour_invalid_format():
    """Test invalid time formats."""
    with pytest.raises(ValueError):
        convert_to_24_hour("9:00 AM")  # Invalid format (contains minutes)
    
    with pytest.raises(ValueError):
        convert_to_24_hour("9 PM 2024")  # Invalid format (contains year)

    with pytest.raises(ValueError):
        convert_to_24_hour("25 AM")  # Invalid hour (out of range)

    with pytest.raises(ValueError):
        convert_to_24_hour("AB CD")  # Invalid time string


def test_convert_to_24_hour_edge_cases():
    """Test edge cases like noon and midnight."""
    assert convert_to_24_hour("12 AM") == 0  # Midnight should be 0
    assert convert_to_24_hour("12 PM") == 12  # Noon should be 12
