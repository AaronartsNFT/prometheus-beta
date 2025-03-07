import os
import pytest
import tempfile

from src.directory_file_size import get_total_directory_size

def test_get_total_directory_size_empty_directory():
    """Test total size of an empty directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        assert get_total_directory_size(temp_dir) == 0

def test_get_total_directory_size_single_file():
    """Test total size with a single file."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a file with known size
        test_file_path = os.path.join(temp_dir, 'test.txt')
        with open(test_file_path, 'wb') as f:
            f.write(b'Hello, World!')
        
        file_size = os.path.getsize(test_file_path)
        assert get_total_directory_size(temp_dir) == file_size

def test_get_total_directory_size_multiple_files():
    """Test total size with multiple files."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create multiple files
        file_sizes = [10, 20, 30]
        total_size = 0
        
        for i, size in enumerate(file_sizes):
            file_path = os.path.join(temp_dir, f'test{i}.txt')
            with open(file_path, 'wb') as f:
                f.write(b'x' * size)
            total_size += size
        
        assert get_total_directory_size(temp_dir) == total_size

def test_get_total_directory_size_nested_files():
    """Test total size with files in nested directories."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create nested directory structure
        nested_dir = os.path.join(temp_dir, 'nested')
        os.makedirs(nested_dir)
        
        # Create files in both main and nested directories
        main_file_path = os.path.join(temp_dir, 'main.txt')
        nested_file_path = os.path.join(nested_dir, 'nested.txt')
        
        with open(main_file_path, 'wb') as f:
            f.write(b'Main file content')
        
        with open(nested_file_path, 'wb') as f:
            f.write(b'Nested file content')
        
        total_size = os.path.getsize(main_file_path) + os.path.getsize(nested_file_path)
        assert get_total_directory_size(temp_dir) == total_size

def test_get_total_directory_size_invalid_input():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        get_total_directory_size(123)
    
    with pytest.raises(TypeError):
        get_total_directory_size(None)

def test_get_total_directory_size_nonexistent_directory():
    """Test error handling for nonexistent directory."""
    with pytest.raises(FileNotFoundError):
        get_total_directory_size('/path/to/nonexistent/directory')

def test_get_total_directory_size_not_a_directory():
    """Test error handling for a path that is not a directory."""
    with tempfile.NamedTemporaryFile() as temp_file:
        with pytest.raises(NotADirectoryError):
            get_total_directory_size(temp_file.name)