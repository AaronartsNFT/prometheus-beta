def find_missing_numbers(arr):
    """
    Find all missing numbers between the smallest and largest numbers in a sorted array.

    Args:
        arr (list): A sorted list of integers in ascending order.

    Returns:
        list: A list of missing numbers between the smallest and largest numbers.

    Raises:
        ValueError: If the input array is empty or None.
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate input
    if arr is None:
        raise ValueError("Input array cannot be None")
    
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    # Validate that input is a list of integers
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    # If there's only one element, return an empty list
    if len(arr) == 1:
        return []
    
    # Find missing numbers
    missing_numbers = []
    for i in range(arr[0] + 1, arr[-1]):
        if i not in arr:
            missing_numbers.append(i)
    
    return missing_numbers