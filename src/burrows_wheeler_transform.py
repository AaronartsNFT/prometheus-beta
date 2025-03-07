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
    
    # Create first column by sorting characters
    first_column = sorted(bwt)
    
    # Create last column (which is the input BWT)
    last_column = list(bwt)
    
    # Reconstruct the original string
    reconstructed = []
    current_char = '$'  # Start from terminator
    
    # Reconstruct the original string by tracing back
    for _ in range(len(bwt)):
        # Find the index of current character in first column
        index = first_column.index(current_char)
        
        # Adjust index if multiple occurrences exist
        # by tracking the occurrence number
        current_occurrences = last_column[:index].count(current_char)
        while current_occurrences > 0:
            index = first_column.index(current_char, index + 1)
            current_occurrences -= 1
        
        # Move to the corresponding character in last column
        current_char = last_column[index]
        reconstructed.append(current_char)
    
    # Remove terminator and return original string
    return ''.join(reconstructed[:-1])