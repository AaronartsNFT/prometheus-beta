import pytest
import random
from src.random_case_converter import convert_to_random_case

def test_convert_to_random_case_basic():
    """Test basic string conversion."""
    input_str = "hello world"
    result = convert_to_random_case(input_str)
    
    # Verify the result is the same length
    assert len(result) == len(input_str)
    
    # Verify alphabetic characters are either upper or lower case
    # Non-alphabetic characters can remain unchanged
    assert all(
        char.isupper() or char.islower() or not char.isalpha() 
        for char in result
    )

def test_convert_to_random_case_empty_string():
    """Test empty string conversion."""
    assert convert_to_random_case("") == ""

def test_convert_to_random_case_invalid_input():
    """Test invalid input types."""
    with pytest.raises(TypeError):
        convert_to_random_case(123)
    with pytest.raises(TypeError):
        convert_to_random_case(None)

def test_convert_to_random_case_randomness():
    """
    Test the randomness of the conversion.
    This test checks that multiple runs are likely to produce different results.
    """
    # Set a fixed seed for reproducibility
    random.seed(42)
    
    input_str = "hello world"
    
    # Generate multiple conversions
    conversions = [convert_to_random_case(input_str) for _ in range(5)]
    
    # Check that at least some conversions are different
    assert len(set(conversions)) > 1, "Random case conversion is not working correctly"

def test_convert_to_random_case_preserves_non_alphabetic():
    """Test that non-alphabetic characters remain unchanged."""
    input_str = "hello123 world!"
    result = convert_to_random_case(input_str)
    
    # Check that non-alphabetic characters remain the same
    assert result[5] == '1'
    assert result[6] == '2'
    assert result[7] == '3'
    assert result[8] == ' '
    assert result[13] == '!'