import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from xz_compression import xz_compress, xz_decompress

def test_xz_compression_string():
    """Test compression and decompression of a string"""
    original_data = "Hello, world! This is a test of XZ compression."
    compressed = xz_compress(original_data)
    assert compressed is not None
    assert len(compressed) < len(original_data.encode('utf-8'))
    
    decompressed = xz_decompress(compressed)
    assert decompressed.decode('utf-8') == original_data

def test_xz_compression_bytes():
    """Test compression and decompression of bytes"""
    original_data = b"Binary data test for XZ compression"
    compressed = xz_compress(original_data)
    assert compressed is not None
    assert len(compressed) < len(original_data)
    
    decompressed = xz_decompress(compressed)
    assert decompressed == original_data

def test_xz_compression_levels():
    """Test different compression levels"""
    data = "Test data for compression levels"
    compressed_level0 = xz_compress(data, compression_level=0)
    compressed_level9 = xz_compress(data, compression_level=9)
    
    # Higher compression level should typically result in smaller compressed size
    assert len(compressed_level9) <= len(compressed_level0)

def test_xz_invalid_compression_level():
    """Test invalid compression level raises ValueError"""
    with pytest.raises(ValueError):
        xz_compress("Test", compression_level=10)
    with pytest.raises(ValueError):
        xz_compress("Test", compression_level=-1)

def test_xz_invalid_input_type():
    """Test invalid input type raises TypeError"""
    with pytest.raises(TypeError):
        xz_compress(123)
    with pytest.raises(TypeError):
        xz_decompress("Not bytes")

def test_xz_large_data():
    """Test compression and decompression of large data"""
    large_data = "A" * 100000
    compressed = xz_compress(large_data)
    decompressed = xz_decompress(compressed)
    assert decompressed.decode('utf-8') == large_data

def test_xz_empty_input():
    """Test compression and decompression of empty input"""
    empty_data = ""
    compressed = xz_compress(empty_data)
    decompressed = xz_decompress(compressed)
    assert decompressed.decode('utf-8') == empty_data