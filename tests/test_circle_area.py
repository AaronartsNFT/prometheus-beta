import pytest
import math
from src.circle_area import calculate_circle_area

def test_circle_area_positive_radius():
    """Test area calculation for various positive radii."""
    assert math.isclose(calculate_circle_area(1), math.pi, rel_tol=1e-10)
    assert math.isclose(calculate_circle_area(0), 0, rel_tol=1e-10)
    assert math.isclose(calculate_circle_area(2.5), math.pi * (2.5 ** 2), rel_tol=1e-10)

def test_circle_area_zero_radius():
    """Test area calculation for zero radius."""
    assert calculate_circle_area(0) == 0

def test_circle_area_negative_radius():
    """Test that negative radius raises a ValueError."""
    with pytest.raises(ValueError, match="Radius cannot be negative"):
        calculate_circle_area(-1)

def test_circle_area_invalid_type():
    """Test that invalid input types raise a TypeError."""
    with pytest.raises(TypeError, match="Radius must be a number"):
        calculate_circle_area("not a number")
    with pytest.raises(TypeError, match="Radius must be a number"):
        calculate_circle_area(None)
    with pytest.raises(TypeError, match="Radius must be a number"):
        calculate_circle_area([1, 2, 3])