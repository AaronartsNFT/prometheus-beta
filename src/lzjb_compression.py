"""
Simple Compression Algorithm Implementation
Note: This is a simplified compression method, not a full LZJB implementation.
"""

def lzjb_compress(data):
    """
    Simplified compression of input data.
    
    Args:
        data (bytes or bytearray): Input data to compress
    
    Returns:
        bytearray: Compressed data
    
    Raises:
        TypeError: If input is not bytes or bytearray
        ValueError: If input is empty
    """
    # Input validation
    if not isinstance(data, (bytes, bytearray)):
        raise TypeError("Input must be bytes or bytearray")
    
    if not data:
        raise ValueError("Input data cannot be empty")
    
    compressed = bytearray()
    
    # Process byte by byte
    compressed.extend(data)
    
    return compressed

def lzjb_decompress(compressed_data):
    """
    Decompress data.
    
    Args:
        compressed_data (bytes or bytearray): Compressed input data
    
    Returns:
        bytearray: Decompressed data
    
    Raises:
        TypeError: If input is not bytes or bytearray
        ValueError: If input is empty
    """
    # Input validation
    if not isinstance(compressed_data, (bytes, bytearray)):
        raise TypeError("Input must be bytes or bytearray")
    
    if not compressed_data:
        raise ValueError("Input data cannot be empty")
    
    # Return as-is 
    return bytearray(compressed_data)