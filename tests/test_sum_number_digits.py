import pytest
from src.sum_number_digits import sum_digits

def test_sum_digits_positive_numbers():
    """Test sum_digits with various positive numbers."""
    assert sum_digits(123) == 6
    assert sum_digits(9876) == 30
    assert sum_digits(10) == 1
    assert sum_digits(0) == 0

def test_sum_digits_single_digit():
    """Test sum of digits for single-digit numbers."""
    for i in range(10):
        assert sum_digits(i) == i

def test_sum_digits_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Test negative number
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        sum_digits(-123)
    
    # Test non-integer inputs
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_digits(123.45)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_digits("123")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_digits(None)