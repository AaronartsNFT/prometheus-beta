def quick_sort(arr):
    """
    Implement the Quick Sort algorithm to sort a list in ascending order.
    
    Quick Sort is a divide-and-conquer algorithm that works by selecting a 'pivot' element
    and partitioning the other elements into two sub-arrays according to whether they are 
    less than or greater than the pivot.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: A new sorted list in ascending order.
    
    Raises:
        TypeError: If the input is not a list or contains non-comparable elements.
    """
    # Handle edge cases
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    def _quick_sort(low, high):
        """
        Recursive helper function to perform quick sort on a sublist.
        
        Args:
            low (int): Starting index of the sublist.
            high (int): Ending index of the sublist.
        """
        if low < high:
            # Partition the array
            partition_index = _partition(low, high)
            
            # Recursively sort the left and right subarrays
            _quick_sort(low, partition_index - 1)
            _quick_sort(partition_index + 1, high)
    
    def _partition(low, high):
        """
        Partition the array using the last element as pivot.
        
        Args:
            low (int): Starting index of the sublist.
            high (int): Ending index of the sublist.
        
        Returns:
            int: The partition index.
        """
        # Choose the rightmost element as pivot
        pivot = arr[high]
        
        # Pointer for greater element
        i = low - 1
        
        # Traverse through all elements
        # Compare each element with pivot
        for j in range(low, high):
            try:
                if arr[j] <= pivot:
                    # If element smaller than pivot is found
                    # swap it with the greater element pointed by i
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            except TypeError:
                raise TypeError("List contains elements that cannot be compared")
        
        # Swap the pivot element with the greater element specified by i
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        
        # Return the position from where partition is done
        return i + 1
    
    # Start the quick sort process
    _quick_sort(0, len(arr) - 1)
    
    return arr