def remove_duplicate_words(sentence: str) -> str:
    """
    Remove duplicate words from a string while maintaining the original order.

    Args:
        sentence (str): The input string containing words to be processed.

    Returns:
        str: A new string with duplicate words removed, preserving the original order.

    Examples:
        >>> remove_duplicate_words("the quick brown fox jumps the quick brown fox")
        'the quick brown fox jumps'
        >>> remove_duplicate_words("hello hello world world python python")
        'hello world python'
        >>> remove_duplicate_words("")
        ''
    """
    # Handle empty string case
    if not sentence:
        return ""
    
    # Split the sentence into words
    words = sentence.split()
    
    # Use a set to track seen words while preserving order
    seen_words = set()
    unique_words = []
    
    for word in words:
        # Only add word if it hasn't been seen before
        if word not in seen_words:
            unique_words.append(word)
            seen_words.add(word)
    
    # Join the unique words back into a string
    return " ".join(unique_words)