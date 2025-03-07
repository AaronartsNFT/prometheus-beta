import pytest
import logging
import json
from io import StringIO
import sys

from src.object_logger import log_object

class TestObjectLogger:
    def setup_method(self):
        # Reset logging to a clean state
        logging.getLogger().handlers.clear()
        
        # Create a string buffer to capture log output
        self.log_capture = StringIO()
        self.logger = logging.getLogger()
        self.handler = logging.StreamHandler(self.log_capture)
        self.logger.addHandler(self.handler)
        self.logger.setLevel(logging.INFO)

    def teardown_method(self):
        # Remove the handler after each test
        self.logger.removeHandler(self.handler)
        self.log_capture.close()

    def test_log_simple_dict(self):
        test_dict = {"name": "John", "age": 30}
        log_object(test_dict, logger=self.logger)
        log_output = self.log_capture.getvalue()
        
        # Check that the output contains the dictionary contents
        assert "John" in log_output
        assert "30" in log_output
        assert json.loads(log_output.split("\n", 1)[1])

    def test_log_complex_object(self):
        test_obj = {
            "name": "Alice",
            "details": {
                "age": 25,
                "skills": ["Python", "Data Science"]
            }
        }
        log_object(test_obj, logger=self.logger)
        log_output = self.log_capture.getvalue()
        
        # Verify nested structure is preserved
        assert "Alice" in log_output
        assert "Python" in log_output
        assert json.loads(log_output.split("\n", 1)[1])

    def test_log_with_custom_log_level(self):
        # Capture log for custom log level
        log_lines = []
        handler = logging.Handler()
        handler.emit = lambda record: log_lines.append(record.getMessage())
        
        # Create test logger with the custom handler
        test_logger = logging.getLogger("test_custom_level")
        test_logger.setLevel(logging.DEBUG)
        test_logger.addHandler(handler)
        
        # Log with DEBUG level
        test_dict = {"key": "value"}
        log_object(test_dict, log_level=logging.DEBUG, logger=test_logger)
        
        # Check if the value is in the logged message
        assert any("value" in line for line in log_lines)

    def test_log_with_non_json_serializable_object(self):
        class NonSerializable:
            def __init__(self):
                self.x = 1
            
            def __str__(self):
                return "NonSerializable Object"

        log_object(NonSerializable(), logger=self.logger)
        log_output = self.log_capture.getvalue()
        
        # Verify the object is logged using str() representation
        assert "NonSerializable Object" in log_output

    def test_log_with_default_logger(self):
        # Capture stdout
        captured_output = StringIO()
        sys.stdout = captured_output

        # Use default logger (root logger)
        log_object({"test": "default"})
        
        # Restore stdout
        sys.stdout = sys.__stdout__
        
        # Check if something was printed
        assert captured_output.getvalue()

    def test_log_with_primitive_types(self):
        primitives = [
            42,
            3.14,
            "Hello, World!",
            True,
            None
        ]
        
        for primitive in primitives:
            # Reset the log capture
            self.log_capture.truncate(0)
            self.log_capture.seek(0)
            
            # Capture stdout
            captured_output = StringIO()
            sys.stdout = captured_output
            
            log_object(primitive, logger=self.logger)
            log_output = self.log_capture.getvalue()
            
            # Restore stdout
            sys.stdout = sys.__stdout__
            
            # Verify the primitive is logged and printed, being flexible about representations
            repr_primitive = str(primitive).lower()
            log_repr = log_output.lower()
            assert repr_primitive in log_repr
            assert repr_primitive in captured_output.getvalue().lower()