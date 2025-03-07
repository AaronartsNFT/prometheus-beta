import pytest
from src.quick_sort import quick_sort

def test_quick_sort_normal_list():
    """Test quick sort with a normal list of integers."""
    input_list = [3, 6, 8, 10, 1, 2, 1]
    assert quick_sort(input_list) == [1, 1, 2, 3, 6, 8, 10]

def test_quick_sort_empty_list():
    """Test quick sort with an empty list."""
    assert quick_sort([]) == []

def test_quick_sort_single_element():
    """Test quick sort with a single-element list."""
    assert quick_sort([42]) == [42]

def test_quick_sort_already_sorted():
    """Test quick sort with an already sorted list."""
    input_list = [1, 2, 3, 4, 5]
    assert quick_sort(input_list) == [1, 2, 3, 4, 5]

def test_quick_sort_reverse_sorted():
    """Test quick sort with a reverse-sorted list."""
    input_list = [5, 4, 3, 2, 1]
    assert quick_sort(input_list) == [1, 2, 3, 4, 5]

def test_quick_sort_duplicate_elements():
    """Test quick sort with duplicate elements."""
    input_list = [3, 3, 3, 3, 3]
    assert quick_sort(input_list) == [3, 3, 3, 3, 3]

def test_quick_sort_with_floats():
    """Test quick sort with floating-point numbers."""
    input_list = [3.14, 2.71, 1.41, 0.58]
    assert quick_sort(input_list) == [0.58, 1.41, 2.71, 3.14]

def test_quick_sort_with_strings():
    """Test quick sort with strings."""
    input_list = ['banana', 'apple', 'cherry', 'date']
    assert quick_sort(input_list) == ['apple', 'banana', 'cherry', 'date']

def test_quick_sort_does_not_modify_original():
    """Ensure the original list is not modified."""
    input_list = [3, 1, 4, 1, 5, 9]
    original_copy = input_list.copy()
    quick_sort(input_list)
    assert input_list == original_copy

def test_quick_sort_invalid_input():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError):
        quick_sort("not a list")

def test_quick_sort_uncomparable_elements():
    """Test that TypeError is raised for uncomparable elements."""
    with pytest.raises(TypeError):
        quick_sort([1, 2, "three", 4])