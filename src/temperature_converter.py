def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    
    Args:
        celsius (float): Temperature in Celsius degrees.
    
    Returns:
        float: Temperature converted to Fahrenheit, rounded to 2 decimal places.
    
    Raises:
        TypeError: If input is not a number.
    """
    # Check if input is a valid number
    if not isinstance(celsius, (int, float)):
        raise TypeError("Input must be a number")
    
    # Conversion formula: (°C × 9/5) + 32 = °F
    fahrenheit = (celsius * 9/5) + 32
    
    # Round to 2 decimal places to handle floating-point precision
    return round(fahrenheit, 2)