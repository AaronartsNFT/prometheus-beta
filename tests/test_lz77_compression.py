import pytest
from src.lz77_compression import LZ77Compressor

def test_lz77_compression_empty_input():
    """Test compression and decompression of empty input."""
    compressor = LZ77Compressor()
    data = b''
    compressed = compressor.compress(data)
    assert compressed == []
    assert compressor.decompress(compressed) == b''

def test_lz77_compression_simple_string():
    """Test compression and decompression of a simple string."""
    compressor = LZ77Compressor()
    data = b'AAAAABBBBB'
    compressed = compressor.compress(data)
    decompressed = compressor.decompress(compressed)
    assert decompressed == data

def test_lz77_compression_repeated_pattern():
    """Test compression of a string with repeated patterns."""
    compressor = LZ77Compressor()
    data = b'abcabcabcabc'
    compressed = compressor.compress(data)
    decompressed = compressor.decompress(compressed)
    assert decompressed == data

def test_lz77_compression_mixed_patterns():
    """Test compression of a string with mixed repeated and unique patterns."""
    compressor = LZ77Compressor()
    data = b'Hello, hello, hello world!'
    compressed = compressor.compress(data)
    decompressed = compressor.decompress(compressed)
    assert decompressed == data

def test_lz77_compression_unicode_string():
    """Test compression of a unicode string."""
    compressor = LZ77Compressor()
    data = '你好，世界！世界很大！'.encode('utf-8')
    compressed = compressor.compress(data)
    decompressed = compressor.decompress(compressed)
    assert decompressed == data

def test_lz77_custom_buffer_sizes():
    """Test compression with custom window and look-ahead buffer sizes."""
    compressor = LZ77Compressor(window_size=128, look_ahead_buffer_size=32)
    data = b'abcdefghijklmnopqrstuvwxyz' * 10
    compressed = compressor.compress(data)
    decompressed = compressor.decompress(compressed)
    assert decompressed == data

def test_lz77_compression_large_input():
    """Test compression of a larger input to ensure performance."""
    compressor = LZ77Compressor()
    data = b'A' * 1000 + b'B' * 1000 + b'A' * 1000
    compressed = compressor.compress(data)
    decompressed = compressor.decompress(compressed)
    assert decompressed == data

def test_lz77_random_byte_sequence():
    """Test compression of a random byte sequence."""
    import os
    compressor = LZ77Compressor()
    data = os.urandom(1024)
    compressed = compressor.compress(data)
    decompressed = compressor.decompress(compressed)
    assert decompressed == data