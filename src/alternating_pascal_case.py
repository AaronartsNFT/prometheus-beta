def convert_to_alternating_pascal_case(input_string: str) -> str:
    """
    Convert a given string to alternating Pascal case.
    
    In alternating Pascal case, words are converted to Pascal case 
    (first letter capitalized, rest lowercase) in an alternating pattern.
    
    Args:
        input_string (str): The input string to convert
    
    Returns:
        str: The string converted to alternating Pascal case
    
    Raises:
        TypeError: If input is not a string
    
    Examples:
        >>> convert_to_alternating_pascal_case("hello world")
        'HelloWorld'
        >>> convert_to_alternating_pascal_case("python is awesome")
        'PythonIsAwesome'
        >>> convert_to_alternating_pascal_case("a b c")
        'ABc'
    """
    # Validate input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not input_string:
        return ""
    
    # Split the string into words, removing extra whitespace
    words = input_string.split()
    
    # If no words, return empty string
    if not words:
        return ""
    
    # Convert words to alternating Pascal case
    result_words = []
    for i, word in enumerate(words):
        # Capitalize based on index
        if i % 2 == 0:
            # For even indexes (0, 2, 4...), first letter uppercase, rest lowercase
            result_words.append(word[0].upper() + word[1:].lower())
        else:
            # For odd indexes (1, 3, 5...), first letter uppercase, rest lowercase
            result_words.append(word[0].upper() + word[1:].lower())
    
    # Join the words without spaces
    return ''.join(result_words)