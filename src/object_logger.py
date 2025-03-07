import json
import logging
import sys

def log_object(obj, log_level=logging.INFO, logger=None):
    """
    Log an object in a readable, pretty-printed JSON format.

    Args:
        obj (Any): The object to be logged
        log_level (int, optional): Logging level. Defaults to logging.INFO.
        logger (logging.Logger, optional): Custom logger. 
                                           If None, uses root logger and prints to stdout.

    Raises:
        TypeError: If the object cannot be serialized to JSON
    """
    # Use root logger if no logger is provided
    if logger is None:
        # Log and print to stdout for default logger
        logger = logging.getLogger()
        
        # Add stdout handler if not exists
        stdout_handler = logging.StreamHandler(sys.stdout)
        if not any(isinstance(h, logging.StreamHandler) for h in logger.handlers):
            logger.addHandler(stdout_handler)

    try:
        # Convert the object to a formatted JSON string
        # Use str for non-JSON serializable objects as a fallback
        def default_serializer(o):
            try:
                # Attempt to use object's __str__ method if json.dumps fails
                return str(o)
            except Exception:
                return repr(o)

        try:
            # First try standard JSON serialization
            formatted_obj = json.dumps(obj, indent=2)
        except TypeError:
            # Fallback to using str() if JSON serialization fails
            formatted_obj = json.dumps(obj, indent=2, default=default_serializer)
        
        # Log the formatted object at the specified log level
        log_message = f"Logged object:\n{formatted_obj}"
        logger.log(log_level, log_message)
    except Exception as e:
        # Handle any unexpected serialization errors
        error_msg = f"Unable to log object: {str(e)}"
        logger.error(error_msg)
        raise TypeError(error_msg)