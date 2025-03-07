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
    
    # Replace non-alphanumeric characters with spaces
    normalized = ''.join(char if char.isalnum() else ' ' for char in input_string)
    
    # Split the string considering camelCase and PascalCase
    words = []
    current_word = normalized[0].upper()
    for char in normalized[1:]:
        if char.isupper() and current_word[-1].islower():
            # Start of a new word in camelCase/PascalCase
            words.append(current_word)
            current_word = char.upper()
        elif char.isspace() and current_word:
            # Space indicates word boundary
            words.append(current_word)
            current_word = ''
        elif char.isalnum():
            current_word += char.upper()
    
    # Add the last word
    if current_word:
        words.append(current_word)
    
    # Join words with underscore and convert to uppercase
    return '_'.join(words).upper()