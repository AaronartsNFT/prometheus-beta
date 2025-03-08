import pytest
from src.mountain_range_generator import create_mountain_range, Mountain

def test_create_mountain_range_basic():
    """Test creating a mountain range with a specific number of peaks"""
    num_peaks = 5
    mountain_range = create_mountain_range(num_peaks)
    
    # Check correct number of peaks
    assert len(mountain_range) == num_peaks
    
    # Verify each item is a Mountain object
    assert all(isinstance(mountain, Mountain) for mountain in mountain_range)

def test_create_mountain_range_single_peak():
    """Test creating a mountain range with a single peak"""
    mountain_range = create_mountain_range(1)
    
    assert len(mountain_range) == 1
    assert isinstance(mountain_range[0], Mountain)

def test_create_mountain_range_invalid_inputs():
    """Test error handling for invalid inputs"""
    # Test negative number of peaks
    with pytest.raises(ValueError, match="Number of peaks must be at least 1"):
        create_mountain_range(0)
    
    # Test negative number of peaks
    with pytest.raises(ValueError, match="Number of peaks must be at least 1"):
        create_mountain_range(-3)
    
    # Test non-integer input
    with pytest.raises(TypeError, match="Number of peaks must be an integer"):
        create_mountain_range(3.5)
    
    with pytest.raises(TypeError, match="Number of peaks must be an integer"):
        create_mountain_range("5")

def test_mountain_object_properties():
    """Test the properties of generated Mountain objects"""
    mountain_range = create_mountain_range(3)
    
    for mountain in mountain_range:
        # Check name
        assert isinstance(mountain.name, str)
        assert mountain.name is not None
        
        # Check height
        assert isinstance(mountain.height, float)
        assert 100 <= mountain.height <= 8848
        
        # Check terrain type
        assert isinstance(mountain.terrain_type, str)
        assert mountain.terrain_type in [
            "alpine", "volcanic", "plateau", 
            "coastal", "desert", "tropical"
        ]

def test_unique_mountain_names():
    """Ensure unique mountain names in a range"""
    mountain_range = create_mountain_range(10)
    
    # Check no duplicate names
    names = [mountain.name for mountain in mountain_range]
    assert len(names) == len(set(names))