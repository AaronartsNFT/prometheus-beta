import re
import pytest
from src.uuid_generator import generate_uuid

def test_uuid_generation():
    """Test that the generated UUID meets basic format requirements."""
    uuid = generate_uuid()
    
    # Check UUID format (8-4-4-4-12 hex characters)
    uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
    assert re.match(uuid_pattern, uuid, re.IGNORECASE), f"Invalid UUID format: {uuid}"

def test_uuid_uniqueness():
    """Test that multiple generated UUIDs are unique."""
    num_uuids = 1000
    generated_uuids = set()
    
    for _ in range(num_uuids):
        uuid = generate_uuid()
        generated_uuids.add(uuid)
    
    # Ensure all UUIDs are unique
    assert len(generated_uuids) == num_uuids, "UUIDs are not unique"

def test_uuid_version():
    """Verify the UUID version is 4."""
    uuid = generate_uuid()
    version_char = uuid.split('-')[2][0]
    assert version_char == '4', f"Incorrect UUID version: {version_char}"

def test_uuid_variant():
    """Verify the UUID variant is correct (8, 9, A, or B in the 7th character)."""
    uuid = generate_uuid()
    variant_char = uuid.split('-')[3][0]
    assert variant_char in '89ab', f"Incorrect UUID variant: {variant_char}"

def test_uuid_length():
    """Verify the total length of the UUID."""
    uuid = generate_uuid()
    assert len(uuid) == 36, f"Incorrect UUID length: {len(uuid)}"