def burrows_wheeler_transform(text):
    """
    Perform the Burrows-Wheeler Transform on the given input text.
    
    The Burrows-Wheeler Transform is a reversible string transformation used 
    in data compression algorithms. It rearranges the characters of a string 
    to improve compression efficiency.
    
    Args:
        text (str): The input string to transform.
    
    Returns:
        tuple: A tuple containing the Burrows-Wheeler transformed string 
               and the original row index (for inverse transform).
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input string is empty.
    """
    # Validate input
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    if not text:
        raise ValueError("Input string cannot be empty")
    
    # Add a special terminator character to handle edge cases
    text_with_terminator = text + '$'
    
    # Generate all rotations of the text
    rotations = [text_with_terminator[i:] + text_with_terminator[:i] 
                 for i in range(len(text_with_terminator))]
    
    # Sort the rotations lexicographically
    sorted_rotations = sorted(rotations)
    
    # Find the index of the original string in the sorted rotations
    original_index = sorted_rotations.index(text_with_terminator)
    
    # Extract the last character of each sorted rotation to form the BWT
    bwt = ''.join(rotation[-1] for rotation in sorted_rotations)
    
    return bwt, original_index

def inverse_burrows_wheeler_transform(bwt_with_index):
    """
    Reverse the Burrows-Wheeler Transform to recover the original text.
    
    Args:
        bwt_with_index: Either the transformed string or a tuple of 
                        (transformed string, original row index)
    
    Returns:
        str: The original text before transformation.
    
    Raises:
        TypeError: If input is not a string or tuple.
        ValueError: If input is empty.
    """
    # Handle different input types 
    if isinstance(bwt_with_index, tuple):
        bwt, original_index = bwt_with_index
    else:
        bwt = bwt_with_index
        original_index = 0
    
    # Validate input
    if not isinstance(bwt, str):
        raise TypeError("Input must be a string")
    
    if not bwt:
        raise ValueError("Input string cannot be empty")
    
    # Sort the characters of the last column
    sorted_chars = sorted(bwt)
    
    # Create the first column 
    first_column = sorted_chars
    
    # Last column (original input)
    last_column = list(bwt)
    
    # Compute next/prev mappings
    n = len(bwt)
    next_mapping = [0] * n
    char_count = {}
    
    for i, char in enumerate(last_column):
        if char not in char_count:
            char_count[char] = 0
        
        # Find the index of this character in the first column
        index = first_column.index(char, char_count[char])
        next_mapping[i] = index
        
        char_count[char] += 1
    
    # Reconstruct the string
    result = []
    current_index = original_index
    
    for _ in range(n - 1):  # Exclude terminator
        # Move to the next character
        current_index = next_mapping[current_index]
        result.append(last_column[current_index])
    
    # Return reversed result 
    return ''.join(reversed(result))