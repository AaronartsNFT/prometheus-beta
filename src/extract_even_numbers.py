def extract_even_numbers(sorted_nums):
    """
    Extract even numbers from a sorted list while maintaining their original order.
    
    Args:
        sorted_nums (list): A sorted list of unique integers.
    
    Returns:
        list: A new list containing only the even numbers from the input list.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list is not sorted in ascending order.
    """
    # Check if input is a list
    if not isinstance(sorted_nums, list):
        raise TypeError("Input must be a list")
    
    # If list is empty, return empty list
    if not sorted_nums:
        return []
    
    # Validate that the list is sorted
    if any(sorted_nums[i] > sorted_nums[i+1] for i in range(len(sorted_nums)-1)):
        raise ValueError("Input list must be sorted in ascending order")
    
    # Extract even numbers using list comprehension (O(n) time complexity)
    return [num for num in sorted_nums if num % 2 == 0]