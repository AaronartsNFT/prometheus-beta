def bucket_sort(arr):
    """
    Implement the bucket sort algorithm for sorting a list of numbers.
    
    Args:
        arr (list): A list of numeric values to be sorted.
    
    Returns:
        list: A new sorted list containing the same elements as the input.
    
    Raises:
        TypeError: If the input is not a list or contains non-numeric values.
        ValueError: If the input list is empty.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if len(arr) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Check if all elements are numeric
    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("All elements must be numeric")
    
    # Find the range of input values
    if len(arr) <= 1:
        return arr.copy()
    
    # Determine the number of buckets (typically sqrt of array length)
    num_buckets = max(int(len(arr) ** 0.5), 1)
    
    # Find min and max values to determine bucket range
    min_val = min(arr)
    max_val = max(arr)
    
    # Handle case where all elements are the same
    if min_val == max_val:
        return arr.copy()
    
    # Create empty buckets
    buckets = [[] for _ in range(num_buckets)]
    
    # Distribute elements into buckets
    bucket_range = (max_val - min_val) / num_buckets
    
    for num in arr:
        # Calculate which bucket the number belongs to
        index = min(int((num - min_val) / bucket_range), num_buckets - 1)
        buckets[index].append(num)
    
    # Sort individual buckets
    sorted_buckets = [sorted(bucket) for bucket in buckets]
    
    # Merge sorted buckets
    return [num for bucket in sorted_buckets for num in bucket]