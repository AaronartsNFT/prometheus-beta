import pytest
from src.find_missing_numbers import find_missing_numbers

def test_find_missing_numbers_basic():
    """Test finding missing numbers in a basic scenario."""
    assert find_missing_numbers([1, 3, 5]) == [2, 4]

def test_find_missing_numbers_consecutive():
    """Test an array with no missing numbers."""
    assert find_missing_numbers([1, 2, 3, 4, 5]) == []

def test_find_missing_numbers_large_range():
    """Test finding missing numbers in a larger range."""
    assert find_missing_numbers([10, 20, 30]) == list(range(11, 20)) + list(range(21, 30))

def test_find_missing_numbers_single_element():
    """Test an array with a single element."""
    assert find_missing_numbers([5]) == []

def test_find_missing_numbers_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input array cannot be None"):
        find_missing_numbers(None)
    
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_missing_numbers([])

def test_find_missing_numbers_type_error():
    """Test handling of non-integer inputs."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        find_missing_numbers([1, 2, '3'])
        
def test_find_missing_numbers_negative_numbers():
    """Test finding missing numbers with negative values."""
    assert find_missing_numbers([-5, -2]) == [-4, -3]