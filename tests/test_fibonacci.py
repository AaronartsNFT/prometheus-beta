import pytest
from src.fibonacci import recursive_fibonacci

def test_fibonacci_base_cases():
    """Test the base cases of the Fibonacci sequence."""
    assert recursive_fibonacci(0) == 0
    assert recursive_fibonacci(1) == 1

def test_fibonacci_early_sequence():
    """Test early Fibonacci numbers."""
    assert recursive_fibonacci(2) == 1
    assert recursive_fibonacci(3) == 2
    assert recursive_fibonacci(4) == 3
    assert recursive_fibonacci(5) == 5
    assert recursive_fibonacci(6) == 8

def test_fibonacci_larger_numbers():
    """Test larger Fibonacci numbers."""
    assert recursive_fibonacci(10) == 55
    assert recursive_fibonacci(15) == 610

def test_fibonacci_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Test negative input
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        recursive_fibonacci(-1)
    
    # Test non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        recursive_fibonacci(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        recursive_fibonacci("5")

def test_fibonacci_performance_warning():
    """
    This test serves as a warning about the performance 
    of recursive Fibonacci implementation.
    Note: For large n, this implementation becomes very slow.
    """
    # Test a moderately sized number that should still compute quickly
    assert recursive_fibonacci(20) == 6765