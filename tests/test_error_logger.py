import logging
import pytest
import io
import sys
from src.error_logger import log_error, log_error_decorator

class TestErrorLogger:
    def setup_method(self):
        # Capture log output
        self.log_capture = io.StringIO()
        self.log_handler = logging.StreamHandler(self.log_capture)
        logging.getLogger().addHandler(self.log_handler)
        logging.getLogger().setLevel(logging.DEBUG)

    def teardown_method(self):
        # Remove log handler
        logging.getLogger().removeHandler(self.log_handler)
        self.log_capture.close()

    def test_log_error_basic_message(self):
        log_error("Test error message")
        log_output = self.log_capture.getvalue()
        assert "Test error message" in log_output
        assert "ERROR" in log_output.upper()

    def test_log_error_with_exception(self):
        try:
            raise ValueError("Test exception")
        except ValueError as e:
            log_error("Custom error message", error=e)
        
        log_output = self.log_capture.getvalue()
        assert "Custom error message" in log_output
        assert "Test exception" in log_output

    def test_log_error_invalid_inputs(self):
        with pytest.raises(TypeError):
            log_error(123)  # Non-string message
        
        with pytest.raises(TypeError):
            log_error("Message", log_level="invalid")  # Non-integer log level

    def test_log_error_decorator(self):
        @log_error_decorator("Custom decorator error")
        def error_function():
            raise RuntimeError("Test runtime error")
        
        with pytest.raises(RuntimeError):
            error_function()
        
        log_output = self.log_capture.getvalue()
        assert "Custom decorator error" in log_output
        assert "Test runtime error" in log_output

    def test_log_error_decorator_with_default_message(self):
        @log_error_decorator()
        def another_error_function():
            raise KeyError("Test key error")
        
        with pytest.raises(KeyError):
            another_error_function()
        
        log_output = self.log_capture.getvalue()
        assert "Error in function another_error_function" in log_output
        assert "Test key error" in log_output