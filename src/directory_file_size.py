import os

def get_total_directory_size(directory_path):
    """
    Calculate the total size of all files in a given directory.

    Args:
        directory_path (str): Path to the directory to calculate file sizes for.

    Returns:
        int: Total size of all files in bytes.

    Raises:
        TypeError: If directory_path is not a string.
        FileNotFoundError: If the specified directory does not exist.
        NotADirectoryError: If the specified path is not a directory.
        PermissionError: If access to the directory is denied.
    """
    # Validate input type
    if not isinstance(directory_path, str):
        raise TypeError("Directory path must be a string")

    # Validate directory exists and is a directory
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"Directory not found: {directory_path}")
    
    if not os.path.isdir(directory_path):
        raise NotADirectoryError(f"Path is not a directory: {directory_path}")

    total_size = 0
    
    try:
        # Walk through all files in the directory and its subdirectories
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                # Use lstat to get file size without following symlinks
                total_size += os.lstat(file_path).st_size
        
        return total_size
    
    except PermissionError:
        raise PermissionError(f"Permission denied accessing directory: {directory_path}")