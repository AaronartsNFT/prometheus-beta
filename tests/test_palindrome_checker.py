import pytest
from src.palindrome_checker import is_palindrome

def test_classic_palindromes():
    """Test classic palindrome scenarios"""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_simple_palindromes():
    """Test simple palindrome scenarios"""
    assert is_palindrome("racecar") == True
    assert is_palindrome("Able was I ere I saw Elba") == True

def test_edge_cases():
    """Test edge cases"""
    assert is_palindrome("") == True  # Empty string
    assert is_palindrome(" ") == True  # Just whitespace
    assert is_palindrome("a") == True  # Single character
    
def test_special_characters():
    """Test with various special characters"""
    assert is_palindrome("Was it a car or a cat I saw?") == True
    assert is_palindrome("No 'x' in Nixon") == True

def test_case_sensitivity():
    """Ensure function is case-insensitive"""
    assert is_palindrome("RaceCar") == True
    assert is_palindrome("A") == True

def test_non_palindromes():
    """Test non-palindrome scenarios"""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    
def test_numeric_palindromes():
    """Test numeric palindromes"""
    assert is_palindrome("12321") == True
    assert is_palindrome("123 321") == True
    assert is_palindrome("12345") == False