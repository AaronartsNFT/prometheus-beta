import os

def is_directory_exists(path):
    """
    Check if a given path exists and is a directory.

    Args:
        path (str): The path to check for directory existence.

    Returns:
        bool: True if the path exists and is a directory, False otherwise.

    Raises:
        TypeError: If the path is not a string.
    """
    # Check if input is a string
    if not isinstance(path, str):
        raise TypeError("Path must be a string")
    
    # Expand any user home directory references and normalize the path
    expanded_path = os.path.expanduser(path)
    
    # Check if path exists and is a directory
    return os.path.isdir(expanded_path)