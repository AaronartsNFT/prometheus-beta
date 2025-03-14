import pytest
from src.palindrome_checker import is_palindrome

def test_simple_palindromes():
    """Test basic palindrome cases"""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("madam") == True

def test_phrase_palindromes():
    """Test palindrome phrases with spaces and punctuation"""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_non_palindromes():
    """Test strings that are not palindromes"""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    assert is_palindrome("race a car") == False

def test_edge_cases():
    """Test edge cases"""
    # Empty string
    assert is_palindrome("") == True
    
    # Single character
    assert is_palindrome("a") == True
    assert is_palindrome("1") == True
    
    # Mixed case and alphanumeric
    assert is_palindrome("Race121ecar") == True
    assert is_palindrome("123 321") == True
    
    # Strings with various non-alphanumeric characters
    assert is_palindrome("A!b@c#c@b!A") == True
    assert is_palindrome("Hello, World!") == False

def test_whitespace_and_punctuation():
    """Test handling of whitespace and punctuation"""
    assert is_palindrome("   radar   ") == True
    assert is_palindrome("A man, a plan, a canal -- Panama") == True
    
def test_numeric_palindromes():
    """Test numeric palindromes"""
    assert is_palindrome("12321") == True
    assert is_palindrome("45654") == True
    assert is_palindrome("1234") == False