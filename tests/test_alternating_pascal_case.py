import pytest
from src.alternating_pascal_case import convert_to_alternating_pascal_case

def test_basic_conversion():
    """Test basic string conversion to alternating Pascal case."""
    assert convert_to_alternating_pascal_case("hello world") == "HelloWorld"
    assert convert_to_alternating_pascal_case("python is awesome") == "PythonIsAwesome"

def test_single_word():
    """Test conversion of a single word."""
    assert convert_to_alternating_pascal_case("hello") == "Hello"

def test_multiple_words():
    """Test conversion of multiple words with alternating capitalization."""
    assert convert_to_alternating_pascal_case("a b c") == "ABc"
    assert convert_to_alternating_pascal_case("one two three four") == "OneTwoThreeFour"

def test_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_alternating_pascal_case("") == ""

def test_whitespace_only():
    """Test conversion of a string with only whitespace."""
    assert convert_to_alternating_pascal_case("   ") == ""

def test_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        convert_to_alternating_pascal_case(None)
    
    with pytest.raises(TypeError):
        convert_to_alternating_pascal_case(123)
    
    with pytest.raises(TypeError):
        convert_to_alternating_pascal_case(["hello", "world"])

def test_mixed_case_input():
    """Test conversion of input with mixed case."""
    assert convert_to_alternating_pascal_case("HELLO world PYTHON") == "HelloWorldPython"
    assert convert_to_alternating_pascal_case("hello WORLD python") == "HelloWorldPython"