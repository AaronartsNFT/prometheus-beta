def find_longest_common_prefix(strings):
    """
    Find the longest common prefix among a list of strings.
    
    Args:
        strings (list): A list of strings to find the common prefix for.
    
    Returns:
        str: The longest common prefix. Returns an empty string if no common prefix exists.
    
    Raises:
        TypeError: If input is not a list.
        ValueError: If the input list is empty.
    
    Examples:
        >>> find_longest_common_prefix(["flower", "flow", "flight"])
        'fl'
        >>> find_longest_common_prefix(["dog", "racecar", "car"])
        ''
        >>> find_longest_common_prefix([""])
        ''
    """
    # Check for invalid inputs
    if not isinstance(strings, list):
        raise TypeError("Input must be a list of strings")
    
    # Handle empty list case
    if not strings:
        raise ValueError("Input list cannot be empty")
    
    # Handle single string or empty string cases
    if len(strings) == 1:
        return strings[0]
    
    # Find the shortest string to use as initial prefix
    shortest = min(strings, key=len)
    
    # Iterate through characters of the shortest string
    for i, char in enumerate(shortest):
        # Check if this character matches at the same position in all other strings
        if any(string[i] != char for string in strings):
            return shortest[:i]
    
    # If we've made it through the entire shortest string, it's the common prefix
    return shortest