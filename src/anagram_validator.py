def is_anagram(str1: str, str2: str) -> bool:
    """
    Determine if two strings are valid anagrams of each other.
    
    An anagram is a word or phrase formed by rearranging the letters of another, 
    using all the original letters exactly once.
    
    Args:
        str1 (str): The first input string (lowercase letters only)
        str2 (str): The second input string (lowercase letters only)
    
    Returns:
        bool: True if the strings are anagrams, False otherwise
    
    Raises:
        ValueError: If input strings contain non-lowercase letters
    """
    # Validate input strings
    if not (str1.islower() and str2.islower()):
        raise ValueError("Input strings must contain only lowercase letters")
    
    # Quick length check
    if len(str1) != len(str2):
        return False
    
    # Use character frequency counting
    # Create dictionaries to count character occurrences
    char_count1 = {}
    char_count2 = {}
    
    # Count characters in first string
    for char in str1:
        char_count1[char] = char_count1.get(char, 0) + 1
    
    # Count characters in second string
    for char in str2:
        char_count2[char] = char_count2.get(char, 0) + 1
    
    # Compare character frequencies
    return char_count1 == char_count2