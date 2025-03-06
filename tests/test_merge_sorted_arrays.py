import pytest
from src.merge_sorted_arrays import merge_sorted_arrays

def test_merge_sorted_arrays_basic():
    """Test merging two sorted arrays with positive numbers."""
    arr1 = [1, 3, 5]
    arr2 = [2, 4, 6]
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 3, 4, 5, 6]

def test_merge_sorted_arrays_different_lengths():
    """Test merging sorted arrays of different lengths."""
    arr1 = [1, 2, 7]
    arr2 = [3, 4, 5, 6]
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 3, 4, 5, 6, 7]

def test_merge_sorted_arrays_one_empty():
    """Test merging when one array is empty."""
    arr1 = [1, 2, 3]
    arr2 = []
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 3]

def test_merge_sorted_arrays_both_empty():
    """Test merging when both arrays are empty."""
    arr1 = []
    arr2 = []
    assert merge_sorted_arrays(arr1, arr2) == []

def test_merge_sorted_arrays_with_duplicates():
    """Test merging sorted arrays with duplicate values."""
    arr1 = [1, 2, 2, 3]
    arr2 = [2, 3, 4, 4]
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 2, 2, 3, 3, 4, 4]

def test_merge_sorted_arrays_negative_numbers():
    """Test merging sorted arrays with negative numbers."""
    arr1 = [-5, -3, 0]
    arr2 = [-4, -2, 1]
    assert merge_sorted_arrays(arr1, arr2) == [-5, -4, -3, -2, 0, 1]

def test_merge_sorted_arrays_invalid_input_not_sorted():
    """Test raising ValueError for unsorted input arrays."""
    arr1 = [3, 1, 5]
    arr2 = [2, 4, 6]
    with pytest.raises(ValueError, match="Input arrays must be sorted in ascending order"):
        merge_sorted_arrays(arr1, arr2)

def test_merge_sorted_arrays_invalid_input_type():
    """Test raising TypeError for invalid input types."""
    arr1 = "not a list"
    arr2 = [1, 2, 3]
    with pytest.raises(TypeError, match="Inputs must be lists"):
        merge_sorted_arrays(arr1, arr2)