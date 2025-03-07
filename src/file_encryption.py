import os
from cryptography.fernet import Fernet

def generate_key() -> bytes:
    """
    Generate a new encryption key.
    
    Returns:
        bytes: A new encryption key for Fernet symmetric encryption.
    """
    return Fernet.generate_key()

def encrypt_file(input_path: str, output_path: str, key: bytes = None) -> bytes:
    """
    Encrypt the contents of a file.
    
    Args:
        input_path (str): Path to the input file to be encrypted.
        output_path (str): Path where the encrypted file will be saved.
        key (bytes, optional): Encryption key. If not provided, a new key is generated.
    
    Returns:
        bytes: The encryption key used.
    
    Raises:
        FileNotFoundError: If the input file does not exist.
        PermissionError: If there are permission issues reading/writing files.
    """
    # Validate input file exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # Generate key if not provided
    if key is None:
        key = generate_key()
    
    # Create Fernet cipher with the key
    fernet = Fernet(key)
    
    try:
        # Read input file
        with open(input_path, 'rb') as file:
            file_data = file.read()
        
        # Encrypt the file data
        encrypted_data = fernet.encrypt(file_data)
        
        # Write encrypted data to output file
        with open(output_path, 'wb') as file:
            file.write(encrypted_data)
        
        return key
    
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing files: {input_path}, {output_path}")
    except IOError as e:
        raise IOError(f"IO error during file encryption: {str(e)}")