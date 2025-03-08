from typing import List
from itertools import permutations

def count_anagrams(s: str) -> int:
    """
    Count the number of distinct anagrams in the given string.
    
    An anagram is a sequence of characters formed by rearranging the letters 
    of the original string, using each letter exactly once.
    
    Args:
        s (str): Input string containing only lowercase English letters.
    
    Returns:
        int: Number of distinct anagrams in the string.
    
    Raises:
        ValueError: If the input string contains non-lowercase letters.
    """
    # Validate input
    if not s or not all(c.islower() for c in s):
        raise ValueError("Input must be a non-empty string with only lowercase letters")
    
    # Use a set to track unique sorted representations of anagrams
    distinct_anagrams = set(''.join(p) for p in set(permutations(s)))
    
    # Return count of distinct anagram signatures
    return len(distinct_anagrams)