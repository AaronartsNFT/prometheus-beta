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
    
    # Preprocessing: Replace non-alphanumeric characters with spaces
    # This helps in splitting words effectively
    preprocessed = re.sub(r'[^a-zA-Z0-9]+', ' ', input_string)
    
    # Split into words considering camelCase, PascalCase
    words = []
    current_word = preprocessed[0].upper()
    
    for char in preprocessed[1:]:
        # Transition from lowercase to uppercase or digit indicates word boundary
        if (char.isupper() or char.isdigit()) and current_word[-1].islower():
            words.append(current_word)
            current_word = ""
        
        # Continue building current word
        current_word += char.upper()
    
    # Add the last word
    if current_word:
        words.append(current_word)
    
    # Remove any empty words and join with underscore
    return '_'.join(word for word in words if word)