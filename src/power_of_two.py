def is_power_of_two(n: int) -> bool:
    """
    Check if a given number is a power of two.

    A power of two is a number that can be expressed as 2^k, where k is a non-negative integer.
    Zero and negative numbers are not considered powers of two.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is a power of two, False otherwise.

    Examples:
        >>> is_power_of_two(1)
        True
        >>> is_power_of_two(16)
        True
        >>> is_power_of_two(0)
        False
        >>> is_power_of_two(-4)
        False
        >>> is_power_of_two(3)
        False
    """
    # Check for non-positive numbers
    if n <= 0:
        return False
    
    # A number is a power of two if and only if it has only one bit set in its binary representation
    # We can check this by using bitwise AND with (n-1)
    return (n & (n - 1)) == 0