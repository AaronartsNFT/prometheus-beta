import pytest
from src.anagram_validator import is_anagram

def test_valid_anagrams():
    """Test valid anagram pairs"""
    assert is_anagram("listen", "silent") == True
    assert is_anagram("anagram", "nagaram") == True
    assert is_anagram("rat", "car") == False

def test_empty_strings():
    """Test empty string scenarios"""
    assert is_anagram("", "") == True

def test_same_string():
    """Test identical strings"""
    assert is_anagram("hello", "hello") == True

def test_different_lengths():
    """Test strings of different lengths"""
    assert is_anagram("abc", "abcd") == False
    assert is_anagram("abc", "ab") == False

def test_invalid_input():
    """Test input validation for non-lowercase letters"""
    with pytest.raises(ValueError, match="Input strings must contain only lowercase letters"):
        is_anagram("Hello", "hello")
    
    with pytest.raises(ValueError, match="Input strings must contain only lowercase letters"):
        is_anagram("hello", "Hello")
    
    with pytest.raises(ValueError, match="Input strings must contain only lowercase letters"):
        is_anagram("hello123", "olleh")

def test_repeated_characters():
    """Test anagrams with repeated characters"""
    assert is_anagram("aab", "baa") == True
    assert is_anagram("aab", "aba") == True
    assert is_anagram("aab", "bba") == False