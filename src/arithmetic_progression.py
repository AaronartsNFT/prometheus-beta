def has_arithmetic_progression(nums):
    """
    Determine if any three consecutive numbers in the array form an arithmetic progression.

    An arithmetic progression is a sequence of numbers where the difference 
    between consecutive terms is constant.

    Args:
        nums (list): A list of positive integers.

    Returns:
        bool: True if any three consecutive numbers form an arithmetic progression, 
              False otherwise.

    Raises:
        ValueError: If the input is not a list of positive integers.

    Examples:
        >>> has_arithmetic_progression([1, 2, 3, 4, 5])  # True (1,2,3 is AP)
        True
        >>> has_arithmetic_progression([1, 3, 5, 7, 9])  # True (1,3,5 is AP)
        True
        >>> has_arithmetic_progression([1, 2, 4, 8, 16])  # False
        False
    """
    # Validate input
    if not isinstance(nums, list):
        raise ValueError("Input must be a list")
    
    # Check if there are enough elements to form a trio
    if len(nums) < 3:
        return False
    
    # Check each trio of consecutive numbers
    for i in range(len(nums) - 2):
        # Check if all numbers are positive
        if nums[i] <= 0 or nums[i+1] <= 0 or nums[i+2] <= 0:
            raise ValueError("All numbers must be positive integers")
        
        # Check if the trio forms an arithmetic progression
        # Arithmetic progression means: b - a = c - b
        if nums[i+1] - nums[i] == nums[i+2] - nums[i+1]:
            return True
    
    return False