"""
Test suite for LZ78 compression and decompression functions.
"""

import pytest
from src.lz78_compression import lz78_compress, lz78_decompress

def test_basic_compression_and_decompression():
    """Test simple string compression and decompression."""
    original = "TOBEORNOTTOBEORTOBEORNOT"
    compressed = lz78_compress(original)
    decompressed = lz78_decompress(compressed)
    assert decompressed == original

def test_empty_string():
    """Test handling of empty string."""
    assert lz78_compress("") == []
    assert lz78_decompress([]) == ""

def test_single_character_string():
    """Test compression and decompression of a single character."""
    original = "A"
    compressed = lz78_compress(original)
    decompressed = lz78_decompress(compressed)
    assert decompressed == original

def test_repeated_sequence():
    """Test compression of a string with repeated sequences."""
    original = "ABABABABAB"
    compressed = lz78_compress(original)
    decompressed = lz78_decompress(compressed)
    assert decompressed == original

def test_complex_sequence():
    """Test compression of a complex sequence."""
    original = "hello world hello world hello"
    compressed = lz78_compress(original)
    decompressed = lz78_decompress(compressed)
    assert decompressed == original

def test_invalid_input_types():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        lz78_compress(123)
    with pytest.raises(TypeError):
        lz78_decompress(123)

def test_decompression_invalid_data():
    """Test error handling for invalid compressed data."""
    with pytest.raises(ValueError):
        lz78_decompress([(1, 'a'), (10, 'b')])  # Invalid dictionary index
    with pytest.raises(TypeError):
        lz78_decompress([('a', 'b')])  # Invalid tuple types

def test_large_sequence():
    """Test compression of a large, repetitive sequence."""
    original = "a" * 1000
    compressed = lz78_compress(original)
    decompressed = lz78_decompress(compressed)
    assert decompressed == original