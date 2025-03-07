"""
LZJB Compression Algorithm Implementation

This module provides functions for LZJB compression and decompression.
LZJB is a fast compression algorithm designed for low-overhead compression.
"""

def lzjb_compress(data):
    """
    Compress input data using the LZJB compression algorithm.
    
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
    
    # LZJB compression implementation
    compressed = bytearray()
    
    # Compression context
    copy_dict = {}
    input_len = len(data)
    current_pos = 0
    
    while current_pos < input_len:
        # Look for best match in previous data
        best_match_len = 0
        best_match_dist = 0
        max_look_back = min(current_pos, 1024)  # Typical LZJB window size
        
        for look_back in range(1, max_look_back + 1):
            match_len = 0
            
            # Check for matching sequence
            while (current_pos + match_len < input_len and 
                   data[current_pos + match_len] == data[current_pos - look_back + match_len] and 
                   match_len < 255):
                match_len += 1
            
            # Update best match if found
            if match_len > best_match_len:
                best_match_len = match_len
                best_match_dist = look_back
        
        # Encode based on match
        if best_match_len > 2:
            # Compression token: distance and length
            compressed.append(((best_match_dist - 1) << 3) | (best_match_len - 1))
            current_pos += best_match_len
        else:
            # Literal byte
            compressed.append(data[current_pos])
            current_pos += 1
    
    return compressed

def lzjb_decompress(compressed_data):
    """
    Decompress data compressed with LZJB compression.
    
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
    
    # Decompression implementation
    decompressed = bytearray()
    input_len = len(compressed_data)
    current_pos = 0
    
    while current_pos < input_len:
        token = compressed_data[current_pos]
        current_pos += 1
        
        # Check if literal or back reference
        if token < 32:  # Literal byte
            decompressed.append(token)
        else:
            # Extract distance and length from token
            distance = ((token >> 3) + 1)
            length = (token & 0x07) + 1
            
            # Copy matching sequence
            start = len(decompressed) - distance
            for i in range(length):
                byte = decompressed[start + i]
                decompressed.append(byte)
    
    return decompressed