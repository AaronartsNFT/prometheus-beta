from typing import List

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
    distinct_anagrams = set()
    
    # Generate all possible anagrams
    def generate_anagrams(current: str, remaining: str):
        # Base case: if no remaining letters, add current anagram
        if not remaining:
            distinct_anagrams.add(''.join(sorted(current)))
            return
        
        # Try each remaining letter as the next character
        for i in range(len(remaining)):
            # Choose current letter
            new_current = current + remaining[i]
            # Remove chosen letter from remaining
            new_remaining = remaining[:i] + remaining[i+1:]
            
            # Recursive call
            generate_anagrams(new_current, new_remaining)
    
    # Start generating anagrams
    generate_anagrams('', s)
    
    # Return count of distinct anagram signatures
    return len(distinct_anagrams)