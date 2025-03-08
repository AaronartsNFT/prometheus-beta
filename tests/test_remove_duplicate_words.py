import pytest
from src.remove_duplicate_words import remove_duplicate_words

def test_remove_duplicate_words_basic():
    """Test basic functionality of removing duplicate words."""
    input_str = "the quick brown fox jumps the quick brown fox"
    expected = "the quick brown fox jumps"
    assert remove_duplicate_words(input_str) == expected

def test_remove_duplicate_words_consecutive():
    """Test removing consecutive duplicate words."""
    input_str = "hello hello world world python python"
    expected = "hello world python"
    assert remove_duplicate_words(input_str) == expected

def test_remove_duplicate_words_empty_string():
    """Test behavior with an empty string."""
    assert remove_duplicate_words("") == ""

def test_remove_duplicate_words_no_duplicates():
    """Test a string with no duplicate words."""
    input_str = "python is an awesome programming language"
    assert remove_duplicate_words(input_str) == input_str

def test_remove_duplicate_words_mixed_case():
    """Test that the function is case-sensitive."""
    input_str = "Hello hello HELLO world World"
    expected = "Hello hello HELLO world World"
    assert remove_duplicate_words(input_str) == expected

def test_remove_duplicate_words_single_word():
    """Test a string with a single repeated word."""
    input_str = "python python python"
    expected = "python"
    assert remove_duplicate_words(input_str) == expected