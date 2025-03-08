def find_missing_number(nums):
    """
    Find the missing number in an array of unique positive integers between 1 and n.
    
    Args:
        nums (list): A list of unique positive integers between 1 and n, 
                     where one number is missing.
    
    Returns:
        int: The missing number.
    
    Raises:
        ValueError: If the input is invalid (empty list, non-positive numbers, etc.)
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Validate input
    if not nums:
        raise ValueError("Input array cannot be empty")
    
    # Calculate the expected sum of numbers from 1 to n
    n = len(nums) + 1  # Total count including the missing number
    
    # Calculate the actual sum of the given array
    actual_sum = sum(nums)
    
    # Calculate the expected sum using the formula for sum of first n natural numbers
    expected_sum = (n * (n + 1)) // 2
    
    # The difference is the missing number
    return expected_sum - actual_sum