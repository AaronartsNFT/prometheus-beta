import random
from dataclasses import dataclass

@dataclass
class Mountain:
    """
    Represents a mountain with its key characteristics.
    
    Attributes:
        name (str): Name of the mountain
        height (float): Height of the mountain in meters
        terrain_type (str): Type of terrain the mountain is located in
    """
    name: str
    height: float
    terrain_type: str

def create_mountain_range(num_peaks):
    """
    Generate a list of mountain range objects with specified number of peaks.
    
    Args:
        num_peaks (int): Number of mountain peaks to generate
    
    Returns:
        list: A list of Mountain objects
    
    Raises:
        ValueError: If num_peaks is less than 1
    """
    # Validate input
    if not isinstance(num_peaks, int):
        raise TypeError("Number of peaks must be an integer")
    
    if num_peaks < 1:
        raise ValueError("Number of peaks must be at least 1")
    
    # Predefined terrain types for variety
    terrain_types = [
        "alpine", "volcanic", "plateau", 
        "coastal", "desert", "tropical"
    ]
    
    # Mountain name prefixes
    mountain_prefixes = [
        "Mount", "Peak", "Summit", "Crest", "Ridge"
    ]
    
    # Generate mountain range
    mountain_range = []
    for i in range(num_peaks):
        # Generate random height between 100 and 8848 (height of Everest)
        height = round(random.uniform(100, 8848), 2)
        
        # Generate unique mountain name
        name_prefix = random.choice(mountain_prefixes)
        name = f"{name_prefix} {i+1}"
        
        # Select random terrain type
        terrain = random.choice(terrain_types)
        
        # Create mountain object
        mountain = Mountain(
            name=name,
            height=height,
            terrain_type=terrain
        )
        
        mountain_range.append(mountain)
    
    return mountain_range