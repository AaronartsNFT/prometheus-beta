import pytest
from src.array_reversal import reverse_array

def test_reverse_array_basic():
    """Test reversing a basic list of integers."""
    assert reverse_array([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]

def test_reverse_array_empty():
    """Test reversing an empty list."""
    assert reverse_array([]) == []

def test_reverse_array_single_element():
    """Test reversing a list with a single element."""
    assert reverse_array([42]) == [42]

def test_reverse_array_mixed_types():
    """Test reversing a list with mixed types."""
    assert reverse_array([1, 'a', True, 3.14]) == [3.14, True, 'a', 1]

def test_reverse_array_nested_list():
    """Test reversing a list with nested lists."""
    assert reverse_array([1, [2, 3], 4]) == [4, [2, 3], 1]

def test_reverse_array_invalid_input():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        reverse_array("not a list")
    
    with pytest.raises(TypeError, match="Input must be a list"):
        reverse_array(123)
    
    with pytest.raises(TypeError, match="Input must be a list"):
        reverse_array(None)