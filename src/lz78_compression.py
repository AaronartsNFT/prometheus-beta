"""
LZ78 Compression Algorithm Implementation

This module provides functions for LZ78 compression and decompression.
LZ78 is a dictionary-based lossless compression algorithm that builds 
a dictionary of previously seen sequences during compression.
"""

def lz78_compress(input_string):
    """
    Compress the input string using the LZ78 compression algorithm.
    
    Args:
        input_string (str): The string to be compressed.
    
    Returns:
        list: A list of tuples representing the compressed data.
              Each tuple is (dictionary_index, next_character).
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input is an empty string.
    """
    # Input validation
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    # Initialize dictionary and output
    dictionary = {}
    result = []
    current_dict_index = 1
    
    # Sliding window variables
    current_sequence = ""
    
    for char in input_string:
        # Try to extend current sequence
        potential_sequence = current_sequence + char
        
        # Check if sequence is in dictionary
        matching_index = None
        for index, seq in dictionary.items():
            if seq == potential_sequence:
                matching_index = index
                break
        
        # If sequence not in dictionary, add to result and dictionary
        if matching_index is None:
            # If current_sequence is empty, use 0 as dictionary index
            dict_index = 0 if not current_sequence else \
                next(key for key, value in dictionary.items() if value == current_sequence)
            
            result.append((dict_index, char))
            dictionary[current_dict_index] = potential_sequence
            current_dict_index += 1
            current_sequence = ""
        else:
            # If sequence matches, continue building sequence
            current_sequence = potential_sequence
    
    # Handle remaining sequence
    if current_sequence:
        dict_index = next(key for key, value in dictionary.items() if value == current_sequence)
        result.append((dict_index, ''))
    
    return result

def lz78_decompress(compressed_data):
    """
    Decompress data compressed with the LZ78 algorithm.
    
    Args:
        compressed_data (list): A list of tuples from LZ78 compression.
    
    Returns:
        str: The decompressed original string.
    
    Raises:
        TypeError: If input is not a list of tuples.
        ValueError: If input contains invalid compression data.
    """
    # Input validation
    if not isinstance(compressed_data, list):
        raise TypeError("Input must be a list of tuples")
    
    if not compressed_data:
        return ""
    
    # Check tuple validity
    if not all(isinstance(item, tuple) and len(item) == 2 
               and isinstance(item[0], int) and isinstance(item[1], str) 
               for item in compressed_data):
        raise ValueError("Invalid compressed data format")
    
    # Initialize dictionary and decompression
    dictionary = {0: ""}
    current_dict_index = 1
    result = []
    
    for dict_index, char in compressed_data:
        # Look up the sequence for the dictionary index
        try:
            previous_sequence = dictionary[dict_index]
        except KeyError:
            raise ValueError(f"Invalid dictionary index: {dict_index}")
        
        # Construct current sequence
        current_sequence = previous_sequence + char
        result.append(current_sequence)
        
        # Add to dictionary if not last entry
        if char:  # Only add if not an empty character signaling end of sequence
            dictionary[current_dict_index] = current_sequence
            current_dict_index += 1
    
    return ''.join(result)