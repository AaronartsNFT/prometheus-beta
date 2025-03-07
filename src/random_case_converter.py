import random

def convert_to_random_case(input_string):
    """
    Convert a string to alternating random case.

    Args:
        input_string (str): The input string to convert.

    Returns:
        str: A new string with alphabetic characters randomly converted to upper or lower case.

    Raises:
        TypeError: If input is not a string.
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")

    # Handle empty string case
    if not input_string:
        return ""

    # Convert only alphabetic characters to random case
    return ''.join(
        char.upper() if char.isalpha() and random.choice([True, False]) else char
        for char in input_string
    )