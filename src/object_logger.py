import json
import logging

def log_object(obj, log_level=logging.INFO, logger=None):
    """
    Log an object in a readable, pretty-printed JSON format.

    Args:
        obj (Any): The object to be logged
        log_level (int, optional): Logging level. Defaults to logging.INFO.
        logger (logging.Logger, optional): Custom logger. 
                                           If None, uses root logger.

    Raises:
        TypeError: If the object cannot be serialized to JSON
    """
    # Use root logger if no logger is provided
    if logger is None:
        logger = logging.getLogger()

    try:
        # Convert the object to a formatted JSON string
        formatted_obj = json.dumps(obj, indent=2, default=str)
        
        # Log the formatted object at the specified log level
        logger.log(log_level, f"Logged object:\n{formatted_obj}")
    
    except TypeError as e:
        # Handle objects that can't be serialized
        error_msg = f"Unable to log object: {str(e)}"
        logger.error(error_msg)
        raise TypeError(error_msg)