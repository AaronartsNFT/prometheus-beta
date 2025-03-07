import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.bucket_sort import bucket_sort

def test_bucket_sort_basic():
    """Test basic sorting of a list of integers"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(input_list)
    assert bucket_sort(input_list) == expected

def test_bucket_sort_floats():
    """Test sorting of floating-point numbers"""
    input_list = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    expected = sorted(input_list)
    assert bucket_sort(input_list) == expected

def test_bucket_sort_mixed_numbers():
    """Test sorting of mixed integers and floats"""
    input_list = [5, 2.5, 3, 1.1, 4.4, 2]
    expected = sorted(input_list)
    assert bucket_sort(input_list) == expected

def test_bucket_sort_single_element():
    """Test sorting a list with a single element"""
    input_list = [42]
    assert bucket_sort(input_list) == input_list

def test_bucket_sort_negative_numbers():
    """Test sorting of list with negative numbers"""
    input_list = [-5, -2, -8, -1, -10]
    expected = sorted(input_list)
    assert bucket_sort(input_list) == expected

def test_bucket_sort_already_sorted():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert bucket_sort(input_list) == input_list

def test_bucket_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert bucket_sort(input_list) == expected

def test_bucket_sort_duplicate_values():
    """Test sorting a list with duplicate values"""
    input_list = [3, 3, 1, 1, 2, 2]
    expected = sorted(input_list)
    assert bucket_sort(input_list) == expected

def test_bucket_sort_empty_list_raises_error():
    """Test that empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        bucket_sort([])

def test_bucket_sort_non_list_input_raises_error():
    """Test that non-list input raises a TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        bucket_sort("not a list")

def test_bucket_sort_non_numeric_input_raises_error():
    """Test that list with non-numeric values raises a TypeError"""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        bucket_sort([1, 2, "three", 4])

def test_bucket_sort_all_same_values():
    """Test sorting a list with all same values"""
    input_list = [5, 5, 5, 5, 5]
    assert bucket_sort(input_list) == input_list