import time
import random
import hashlib

def generate_uuid():
    """
    Generate a version 4 UUID (random UUID) without using external libraries.
    
    Returns:
        str: A unique identifier in the standard UUID format (8-4-4-4-12 hexadecimal characters)
    """
    # Get current timestamp and random components
    timestamp = int(time.time() * 1000)
    random_part1 = random.getrandbits(32)
    random_part2 = random.getrandbits(16)
    random_part3 = random.getrandbits(16)
    random_part4 = random.getrandbits(48)
    
    # Create a hash to add more uniqueness
    hash_input = f"{timestamp}{random_part1}{random_part2}{random_part3}{random_part4}"
    hash_object = hashlib.sha1(hash_input.encode())
    hash_hex = hash_object.hexdigest()
    
    # Format the UUID according to version 4 specifications
    # Set the version (4) and variant (8, 9, A, or B) bits
    uuid_parts = [
        hash_hex[:8],  # time-low
        hash_hex[8:12],  # time-mid
        f"4{hash_hex[12:15]}",  # time-high-and-version (forced to version 4)
        f"{hex(int(hash_hex[15], 16) & 3 | 8)[2:]}{hash_hex[16:19]}",  # clock-seq (variant)
        hash_hex[19:31]  # node
    ]
    
    return '-'.join(uuid_parts)