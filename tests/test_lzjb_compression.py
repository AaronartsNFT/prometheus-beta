"""
Test cases for LZJB compression algorithm implementation
"""

import pytest
import random
import string
from src.lzjb_compression import lzjb_compress, lzjb_decompress

def test_basic_compression_decompression():
    """Test basic compression and decompression"""
    original_data = b"hello world hello world"
    compressed = lzjb_compress(original_data)
    decompressed = lzjb_decompress(compressed)
    
    assert decompressed == original_data

def test_random_data_compression():
    """Test compression and decompression with random data"""
    # Generate random byte data
    random.seed(42)
    original_data = bytes(random.randint(0, 255) for _ in range(1000))
    
    compressed = lzjb_compress(original_data)
    decompressed = lzjb_decompress(compressed)
    
    assert decompressed == original_data

def test_repeated_pattern_compression():
    """Test compression of data with repeated patterns"""
    original_data = b"ABCABCABCABCABCABC" * 10
    compressed = lzjb_compress(original_data)
    decompressed = lzjb_decompress(compressed)
    
    assert decompressed == original_data

def test_input_type_validation():
    """Test input type validation"""
    with pytest.raises(TypeError):
        lzjb_compress("not bytes")
    
    with pytest.raises(TypeError):
        lzjb_decompress("not bytes")

def test_empty_input_validation():
    """Test empty input validation"""
    with pytest.raises(ValueError):
        lzjb_compress(b"")
    
    with pytest.raises(ValueError):
        lzjb_decompress(b"")

def test_long_random_text():
    """Test compression and decompression of long random text"""
    # Generate a long random text
    random.seed(123)
    characters = string.ascii_letters + string.digits + string.punctuation
    original_data = ''.join(random.choice(characters) for _ in range(5000)).encode('utf-8')
    
    compressed = lzjb_compress(original_data)
    decompressed = lzjb_decompress(compressed)
    
    assert decompressed == original_data

def test_single_byte_compression():
    """Test compression and decompression of a single byte"""
    original_data = b"A"
    compressed = lzjb_compress(original_data)
    decompressed = lzjb_decompress(compressed)
    
    assert decompressed == original_data