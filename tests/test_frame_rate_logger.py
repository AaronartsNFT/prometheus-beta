"""
Tests for the FrameRateLogger class.

This module contains comprehensive tests to verify 
the functionality of the FrameRateLogger.
"""

import pytest
from src.frame_rate_logger import FrameRateLogger

def test_frame_rate_logger_initialization():
    """Test initialization of FrameRateLogger."""
    logger = FrameRateLogger()
    assert logger is not None
    assert logger.sample_interval == 1000
    assert logger.log_callback == print

def test_custom_log_callback():
    """Test initialization with a custom log callback."""
    def custom_log(msg):
        return msg
    
    logger = FrameRateLogger(log_callback=custom_log)
    assert logger.log_callback == custom_log

def test_start_monitoring():
    """Test the start_monitoring method."""
    logger = FrameRateLogger()
    monitoring_state = logger.start_monitoring()
    
    assert isinstance(monitoring_state, dict)
    assert 'start_time' in monitoring_state
    assert 'frames_rendered' in monitoring_state

def test_calculate_frame_rate():
    """Test frame rate calculation."""
    logger = FrameRateLogger()
    
    # Test with valid state
    state = {
        'start_time': 0,
        'frames_rendered': 60
    }
    fps = logger.calculate_frame_rate(state)
    assert isinstance(fps, float)
    assert fps > 0

def test_calculate_frame_rate_invalid_input():
    """Test frame rate calculation with invalid input."""
    logger = FrameRateLogger()
    
    with pytest.raises(ValueError):
        logger.calculate_frame_rate(None)
    
    with pytest.raises(ValueError):
        logger.calculate_frame_rate("invalid")

def test_log_performance():
    """Test performance logging."""
    logged_data = []
    def capture_log(msg):
        logged_data.append(msg)
    
    logger = FrameRateLogger(log_callback=capture_log)
    
    state = {
        'start_time': 0,
        'frames_rendered': 60
    }
    
    updated_state = logger.log_performance(state)
    
    assert len(logged_data) > 0
    assert 'timestamp' in logged_data[0]
    assert 'fps' in logged_data[0]
    assert updated_state == state

def test_log_performance_error_handling():
    """Test error handling in performance logging."""
    logged_errors = []
    def error_log(msg):
        logged_errors.append(msg)
    
    logger = FrameRateLogger(log_callback=error_log)
    
    # Pass an invalid state to trigger error handling
    logger.log_performance(None)
    
    assert len(logged_errors) > 0
    assert "Performance logging error" in str(logged_errors[0])