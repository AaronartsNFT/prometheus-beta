import os
import pytest
from cryptography.fernet import Fernet
from src.file_encryption import encrypt_file, generate_key

class TestFileEncryption:
    def setup_method(self):
        # Setup directory for test files
        os.makedirs('tests/test_files', exist_ok=True)
    
    def test_generate_key(self):
        """Test key generation produces valid Fernet key"""
        key = generate_key()
        assert isinstance(key, bytes)
        # Verify the key is valid for Fernet
        try:
            Fernet(key)
        except Exception as e:
            pytest.fail(f"Generated key is not a valid Fernet key: {e}")
    
    def test_encrypt_file_with_generated_key(self):
        """Test encrypting a file with an auto-generated key"""
        # Create a test input file
        input_path = 'tests/test_files/input.txt'
        output_path = 'tests/test_files/encrypted.bin'
        
        with open(input_path, 'wb') as f:
            f.write(b'Test encryption content')
        
        # Encrypt the file
        key = encrypt_file(input_path, output_path)
        
        # Verify key was returned and is valid
        assert key is not None
        
        # Verify output file was created
        assert os.path.exists(output_path)
        
        # Verify file contents changed
        with open(input_path, 'rb') as f:
            original_data = f.read()
        
        with open(output_path, 'rb') as f:
            encrypted_data = f.read()
        
        assert original_data != encrypted_data
    
    def test_encrypt_file_with_provided_key(self):
        """Test encrypting a file with a provided key"""
        input_path = 'tests/test_files/input2.txt'
        output_path = 'tests/test_files/encrypted2.bin'
        
        with open(input_path, 'wb') as f:
            f.write(b'Another test content')
        
        # Use a preset key
        test_key = generate_key()
        returned_key = encrypt_file(input_path, output_path, key=test_key)
        
        assert returned_key == test_key
    
    def test_encrypt_nonexistent_file(self):
        """Test that encrypting a nonexistent file raises FileNotFoundError"""
        with pytest.raises(FileNotFoundError):
            encrypt_file('nonexistent_file.txt', 'output.bin')
    
    def teardown_method(self):
        # Clean up test files
        test_dir = 'tests/test_files'
        for file in os.listdir(test_dir):
            os.remove(os.path.join(test_dir, file))
        os.rmdir(test_dir)