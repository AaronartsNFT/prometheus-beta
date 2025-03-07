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
    
    # Create a sorted list of rotations with their original indices
    sorted_rotations_with_indices = sorted(enumerate(rotations), key=lambda x: x[1])
    
    # Find the index of the original string in the sorted rotations
    original_index = next(i for i, (idx, _) in enumerate(sorted_rotations_with_indices) if idx == 0)
    
    # Extract the last character of each sorted rotation to form the BWT
    bwt = ''.join(rotation[-1] for _, rotation in sorted_rotations_with_indices)
    
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
    
    # Create first column by sorting the last column
    first_column = sorted(bwt)
    last_column = list(bwt)
    
    # Create next array to track character positions
    next_arr = [0] * len(bwt)
    char_counts = {}
    
    # Track character occurrences and create the next array
    for i, char in enumerate(last_column):
        count = char_counts.get(char, 0)
        next_index = first_column.index(char, count)
        next_arr[i] = next_index
        char_counts[char] = count + 1
    
    # Reconstruct the original string
    result = []
    current_index = original_index
    
    for _ in range(len(bwt) - 1):  # -1 to remove terminator
        current_index = next_arr[current_index]
        result.append(last_column[current_index])
    
    # Reverse the result and convert to string
    return ''.join(reversed(result))