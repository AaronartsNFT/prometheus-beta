import pytest
from src.power_of_two import is_power_of_two

def test_powers_of_two():
    """Test various powers of two."""
    powers = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    for num in powers:
        assert is_power_of_two(num), f"{num} should be a power of two"

def test_non_powers_of_two():
    """Test numbers that are not powers of two."""
    non_powers = [0, 3, 5, 6, 7, 9, 10, 12, 15, 17, 31, 33]
    for num in non_powers:
        assert not is_power_of_two(num), f"{num} should not be a power of two"

def test_negative_numbers():
    """Test that negative numbers are not considered powers of two."""
    negative_nums = [-1, -2, -4, -8, -16]
    for num in negative_nums:
        assert not is_power_of_two(num), f"{num} should not be a power of two"

def test_large_powers_of_two():
    """Test large powers of two."""
    large_powers = [2**10, 2**20, 2**30]
    for num in large_powers:
        assert is_power_of_two(num), f"{num} should be a power of two"

def test_input_types():
    """Test the function with invalid input types."""
    with pytest.raises(TypeError):
        is_power_of_two(3.14)
    with pytest.raises(TypeError):
        is_power_of_two("16")
    with pytest.raises(TypeError):
        is_power_of_two(None)