import math

def calculate_circle_area(radius):
    """
    Calculate the area of a circle given its radius.

    Args:
        radius (float): The radius of the circle. Must be a non-negative number.

    Returns:
        float: The area of the circle, calculated as π * r^2.

    Raises:
        ValueError: If the radius is negative.
        TypeError: If the radius is not a number.
    """
    # Check for valid input type
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    
    # Check for non-negative radius
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    
    # Calculate and return the area
    return math.pi * radius ** 2