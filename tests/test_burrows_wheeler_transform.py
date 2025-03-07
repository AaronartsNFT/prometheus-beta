import pytest
from src.burrows_wheeler_transform import burrows_wheeler_transform, inverse_burrows_wheeler_transform

def test_burrows_wheeler_transform_basic():
    """Test basic Burrows-Wheeler Transform functionality."""
    text = "banana"
    bwt, index = burrows_wheeler_transform(text)
    assert isinstance(bwt, str)
    assert len(bwt) == len(text) + 1
    assert 0 <= index < len(text) + 1

def test_inverse_transform_recovery():
    """Verify that inverse transform recovers the original text."""
    text = "banana"
    bwt = burrows_wheeler_transform(text)
    recovered = inverse_burrows_wheeler_transform(bwt)
    assert recovered == text

def test_edge_cases():
    """Test edge cases and boundary conditions."""
    # Test single character
    single_char = "a"
    bwt = burrows_wheeler_transform(single_char)
    recovered = inverse_burrows_wheeler_transform(bwt)
    assert recovered == single_char

    # Test repeated characters
    repeated_chars = "aaaa"
    bwt = burrows_wheeler_transform(repeated_chars)
    recovered = inverse_burrows_wheeler_transform(bwt)
    assert recovered == repeated_chars

def test_error_handling():
    """Test error handling for invalid inputs."""
    # Test non-string input
    with pytest.raises(TypeError):
        burrows_wheeler_transform(123)
    
    with pytest.raises(TypeError):
        inverse_burrows_wheeler_transform(456)
    
    # Test empty string
    with pytest.raises(ValueError):
        burrows_wheeler_transform("")
    
    with pytest.raises(ValueError):
        inverse_burrows_wheeler_transform("")

def test_complex_text():
    """Test with a more complex input text."""
    text = "Mississippi River"
    bwt = burrows_wheeler_transform(text)
    recovered = inverse_burrows_wheeler_transform(bwt)
    assert recovered == text