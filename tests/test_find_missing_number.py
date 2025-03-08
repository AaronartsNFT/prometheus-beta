import pytest
from src.find_missing_number import find_missing_number

def test_find_missing_number_basic():
    """Test finding a missing number in a standard scenario."""
    assert find_missing_number([3, 7, 1, 2, 8, 4, 5]) == 6

def test_find_missing_number_sequence_start():
    """Test when the missing number is at the start of the sequence."""
    assert find_missing_number([2, 3, 4, 5, 6, 7, 8]) == 1

def test_find_missing_number_sequence_end():
    """Test when the missing number is at the end of the sequence."""
    assert find_missing_number([1, 2, 3, 4, 5, 6, 7]) == 8

def test_find_missing_number_small_sequence():
    """Test with a small sequence of numbers."""
    assert find_missing_number([1, 3]) == 2

def test_find_missing_number_error_empty_list():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_missing_number([])

def test_find_missing_number_large_sequence():
    """Test with a larger sequence of numbers."""
    # Create a list with 1000 numbers missing 500
    nums = list(range(1, 500)) + list(range(501, 1001))
    assert find_missing_number(nums) == 500