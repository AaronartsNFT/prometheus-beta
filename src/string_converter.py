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
    
    # Process the string to split into words
    words = []
    current_word = ""
    
    for i, char in enumerate(input_string):
        # If not alphanumeric, reset and continue
        if not char.isalnum():
            if current_word:
                words.append(current_word)
                current_word = ""
            continue
        
        # Start a new word for uppercase and number transitions
        if (current_word and 
            ((char.isupper() and not current_word[-1].isupper()) or 
             (char.isdigit() and not current_word[-1].isdigit()))):
            words.append(current_word)
            current_word = ""
        
        # Add character to current word
        current_word += char.upper()
    
    # Add last word if exists
    if current_word:
        words.append(current_word)
    
    # Join words with underscore
    return '_'.join(words)