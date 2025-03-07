"""
LZJB Compression Algorithm Implementation

This module provides functions for LZJB compression and decompression.
LZJB is a fast compression algorithm designed for low-overhead compression.
"""

def lzjb_compress(data):
    """
    Compress input data using a simplified LZJB-like compression algorithm.
    
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
    
    # Compression implementation
    compressed = bytearray()
    input_len = len(data)
    current_pos = 0
    
    while current_pos < input_len:
        # Look back 1024 bytes (typical LZJB sliding window)
        max_look_back = min(current_pos, 1024)
        
        # Find longest matching sequence
        best_match_len = 0
        best_match_dist = 0
        
        for look_back in range(1, max_look_back + 1):
            match_len = 0
            
            # Check for matching sequence
            while (current_pos + match_len < input_len and 
                   match_len < 8 and  # Limit match length to 8 bytes
                   data[current_pos + match_len] == data[current_pos - look_back + match_len]):
                match_len += 1
            
            # Update best match if found
            if match_len > best_match_len:
                best_match_len = match_len
                best_match_dist = look_back
        
        # Encode match or literal byte
        if best_match_len > 2:
            # Encode distance and length 
            # Top 5 bits: distance-1, Bottom 3 bits: length-1
            dist_shift = min(31, best_match_dist - 1)
            len_shift = min(7, best_match_len - 1)
            token = (dist_shift << 3) | len_shift
            compressed.append(token)
            current_pos += best_match_len
        else:
            # Literal byte
            compressed.append(data[current_pos])
            current_pos += 1
    
    return compressed

def lzjb_decompress(compressed_data):
    """
    Decompress data compressed with LZJB-like compression.
    
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
            # Extract distance and length
            distance = ((token >> 3) + 1)
            length = (token & 0x07) + 1
            
            # Safety check 
            if len(decompressed) < distance:
                # Cannot copy from earlier in the stream, append as literal
                decompressed.append(token)
                continue
            
            # Copy matching sequence
            start = len(decompressed) - distance
            for _ in range(length):
                # Append previous byte
                decompressed.append(decompressed[start])
                start += 1
    
    return decompressed