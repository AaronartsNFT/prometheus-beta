import pytest
from src.count_anagrams import count_anagrams

def test_count_anagrams_basic():
    # Basic test cases
    assert count_anagrams('abc') == 6  # a, b, c, ab, ac, bc, abc, bac, etc.
    assert count_anagrams('aab') == 3  # unique anagram signatures

def test_count_anagrams_single_letter():
    # Single letter should always be 1 distinct anagram
    assert count_anagrams('a') == 1

def test_count_anagrams_repeated_letters():
    # Test with repeated letters
    assert count_anagrams('abb') == 3  # a, b, ab, ba, abb

def test_count_anagrams_error_handling():
    # Test error cases
    with pytest.raises(ValueError, match="Input must be a non-empty string with only lowercase letters"):
        count_anagrams('')
    
    with pytest.raises(ValueError, match="Input must be a non-empty string with only lowercase letters"):
        count_anagrams('ABC')
    
    with pytest.raises(ValueError, match="Input must be a non-empty string with only lowercase letters"):
        count_anagrams('ab1')

def test_count_anagrams_longer_string():
    # Test a bit longer string
    assert count_anagrams('abcd') == 24  # 4! = 24 permutations