import pytest
from src.arithmetic_progression import has_arithmetic_progression

def test_has_arithmetic_progression():
    # Test standard arithmetic progressions
    assert has_arithmetic_progression([1, 2, 3, 4, 5]) == True
    assert has_arithmetic_progression([3, 5, 7, 9, 11]) == True
    assert has_arithmetic_progression([2, 4, 6, 8, 10]) == True
    
    # Test cases without arithmetic progression
    assert has_arithmetic_progression([1, 2, 4, 8, 16]) == False
    assert has_arithmetic_progression([1, 3, 6, 10, 15]) == False
    
    # Test edge cases
    assert has_arithmetic_progression([1, 1, 1]) == True
    assert has_arithmetic_progression([2, 2, 2]) == True
    
    # Test short lists
    assert has_arithmetic_progression([1, 2]) == False
    assert has_arithmetic_progression([]) == False

def test_arithmetic_progression_error_handling():
    # Test non-list input
    with pytest.raises(ValueError, match="Input must be a list"):
        has_arithmetic_progression("not a list")
    
    # Test non-positive numbers
    with pytest.raises(ValueError, match="All numbers must be positive integers"):
        has_arithmetic_progression([1, 2, 0])
    
    with pytest.raises(ValueError, match="All numbers must be positive integers"):
        has_arithmetic_progression([1, -2, 3])

def test_different_arithmetic_progressions():
    # Different types of arithmetic progressions
    assert has_arithmetic_progression([10, 7, 4, 1, -2]) == True
    assert has_arithmetic_progression([3, 5, 7, 9, 11]) == True
    assert has_arithmetic_progression([1, 4, 7, 10, 13]) == True