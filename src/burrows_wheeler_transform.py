def burrows_wheeler_transform(text):
    """
    Perform the Burrows-Wheeler Transform on the given input text.
    
    The Burrows-Wheeler Transform is a reversible string transformation used 
    in data compression algorithms. It rearranges the characters of a string 
    to improve compression efficiency.
    
    Args:
        text (str): The input string to transform.
    
    Returns:
        str: The Burrows-Wheeler transformed string.
    
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
    
    # Extract the last character of each sorted rotation to form the BWT
    return ''.join(rotation[-1] for rotation in sorted_rotations)

def inverse_burrows_wheeler_transform(bwt):
    """
    Reverse the Burrows-Wheeler Transform to recover the original text.
    
    Args:
        bwt (str): The Burrows-Wheeler transformed string.
    
    Returns:
        str: The original text before transformation.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input string is empty.
    """
    # Validate input
    if not isinstance(bwt, str):
        raise TypeError("Input must be a string")
    
    if not bwt:
        raise ValueError("Input string cannot be empty")
    
    # Count occurrences of each character
    char_count = {}
    for char in bwt:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Sort the characters of the last column
    sorted_chars = sorted(bwt)
    
    # Create the first column (sorted characters)
    first_column = sorted_chars
    
    # Last column (original input)
    last_column = list(bwt)
    
    # Create the next array
    next_array = {}
    for i, char in enumerate(last_column):
        if char not in next_array:
            next_array[char] = first_column.index(char)
            # Move to the next occurrence for repeated characters
            first_column[next_array[char]] = None
    
    # Reconstruct the original string
    reconstructed = []
    current_char = '$'
    for _ in range(len(bwt) - 1):  # -1 to remove terminator
        current_char = last_column[next_array[current_char]]
        reconstructed.append(current_char)
    
    # Reverse and return (excluding terminator)
    return ''.join(reversed(reconstructed))