import re

def to_constant_case(input_string: str) -> str:
    """
    Convert a given string to CONSTANT_CASE.
    
    Handles various input formats including camelCase, snake_case, 
    PascalCase, and regular strings.
    
    Args:
        input_string (str): The input string to convert
    
    Returns:
        str: The input string converted to CONSTANT_CASE
    
    Raises:
        TypeError: If input is not a string
    
    Examples:
        >>> to_constant_case("hello world")
        'HELLO_WORLD'
        >>> to_constant_case("helloWorld")
        'HELLO_WORLD'
        >>> to_constant_case("hello_world")
        'HELLO_WORLD'
        >>> to_constant_case("HelloWorld")
        'HELLO_WORLD'
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not input_string:
        return ""
    
    # Step 1: Replace non-alphanumeric chars with spaces
    normalized = re.sub(r'[^a-zA-Z0-9]+', ' ', input_string)
    
    # Step 2: Add space before uppercase letters and numbers
    # This handles camelCase, PascalCase, and adjacent numbers
    normalized = re.sub(r'([a-z])([A-Z])', r'\1 \2', normalized)
    normalized = re.sub(r'([a-zA-Z])(\d)', r'\1 \2', normalized)
    normalized = re.sub(r'(\d)([a-zA-Z])', r'\1 \2', normalized)
    
    # Step 3: Split words, convert to uppercase
    words = normalized.upper().split()
    
    # Step 4: Join with underscore
    return '_'.join(words)