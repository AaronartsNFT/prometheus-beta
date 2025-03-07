import os
import pytest
import tempfile
import shutil

from src.directory_utils import is_directory_exists

def test_existing_directory():
    """Test that an existing directory returns True."""
    with tempfile.TemporaryDirectory() as temp_dir:
        assert is_directory_exists(temp_dir) is True

def test_nonexistent_directory():
    """Test that a nonexistent directory returns False."""
    # Create a path that almost certainly doesn't exist
    non_existent_path = "/tmp/definitely_not_a_real_directory_12345"
    assert is_directory_exists(non_existent_path) is False

def test_file_path():
    """Test that a file path returns False."""
    with tempfile.NamedTemporaryFile() as temp_file:
        assert is_directory_exists(temp_file.name) is False

def test_user_home_directory():
    """Test that user home directory expansion works."""
    home_path = "~"
    assert is_directory_exists(home_path) is True

def test_invalid_input_type():
    """Test that invalid input types raise a TypeError."""
    with pytest.raises(TypeError):
        is_directory_exists(123)
    
    with pytest.raises(TypeError):
        is_directory_exists(None)

def test_empty_string():
    """Test handling of an empty string path."""
    assert is_directory_exists("") is False