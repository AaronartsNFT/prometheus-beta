import logging
import traceback
from typing import Optional, Any, Callable

def log_error(message: str, 
              error: Optional[Exception] = None, 
              log_level: int = logging.ERROR, 
              include_traceback: bool = True) -> None:
    """
    Log a custom error message with optional exception details.

    Args:
        message (str): Custom error message to log
        error (Optional[Exception], optional): Exception to log details for. Defaults to None.
        log_level (int, optional): Logging level. Defaults to logging.ERROR.
        include_traceback (bool, optional): Whether to include full traceback. Defaults to True.

    Raises:
        TypeError: If message is not a string or log_level is not an integer
    """
    # Validate input types
    if not isinstance(message, str):
        raise TypeError("Error message must be a string")
    
    if not isinstance(log_level, int):
        raise TypeError("Log level must be an integer")

    # Configure logging if not already configured
    logging.basicConfig(
        level=logging.DEBUG, 
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    # Log the custom message
    logger = logging.getLogger(__name__)
    logger.log(log_level, message)

    # Log exception details if provided
    if error:
        if include_traceback:
            logger.error(f"Exception Details: {str(error)}")
            logger.error("Traceback:\n%s", traceback.format_exc())
        else:
            logger.error(f"Exception: {str(error)}")

def log_error_decorator(log_message: Optional[str] = None):
    """
    Decorator to log errors that occur in a function.

    Args:
        log_message (Optional[str], optional): Custom log message. Defaults to None.

    Returns:
        Callable: Decorated function that logs errors
    """
    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                default_msg = f"Error in function {func.__name__}"
                error_message = log_message or default_msg
                log_error(error_message, error=e)
                raise
        return wrapper
    return decorator