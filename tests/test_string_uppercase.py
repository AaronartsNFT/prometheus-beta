import pytest
from src.string_uppercase import convert_to_uppercase

def test_convert_to_uppercase_basic():
    """Test converting a basic string to uppercase."""
    assert convert_to_uppercase("hello") == "HELLO"
    assert convert_to_uppercase("world") == "WORLD"

def test_convert_to_uppercase_mixed_case():
    """Test converting a mixed-case string to uppercase."""
    assert convert_to_uppercase("HeLLo WoRLd") == "HELLO WORLD"

def test_convert_to_uppercase_empty_string():
    """Test converting an empty string."""
    assert convert_to_uppercase("") == ""

def test_convert_to_uppercase_with_numbers_and_symbols():
    """Test converting a string with numbers and symbols."""
    assert convert_to_uppercase("hello123!@#") == "HELLO123!@#"

def test_convert_to_uppercase_invalid_input():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_uppercase(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_uppercase(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_uppercase(["list"])