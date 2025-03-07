import pytest
from src.longest_common_prefix import find_longest_common_prefix

def test_normal_case():
    """Test finding longest common prefix in a normal scenario"""
    assert find_longest_common_prefix(["flower", "flow", "flight"]) == "fl"

def test_no_common_prefix():
    """Test case with no common prefix"""
    assert find_longest_common_prefix(["dog", "racecar", "car"]) == ""

def test_single_string():
    """Test case with a single string"""
    assert find_longest_common_prefix(["alone"]) == "alone"

def test_empty_string_in_list():
    """Test case with an empty string in the list"""
    assert find_longest_common_prefix(["", "b"]) == ""

def test_all_identical_strings():
    """Test case with identical strings"""
    assert find_longest_common_prefix(["aa", "aa", "aa"]) == "aa"

def test_partial_match():
    """Test case with partial prefix match"""
    assert find_longest_common_prefix(["interspecies", "interstellar", "interstate"]) == "inters"

def test_invalid_input_type():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list of strings"):
        find_longest_common_prefix("not a list")

def test_empty_list():
    """Test raising ValueError for empty list"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_longest_common_prefix([])