import logging  # Importing the logging module for logging functionality

DEBUG_LVL = 12  # Constant representing the debug log level


def get_logger():
    """
    Retrieves a logger instance with a specified log level.

    Returns:
        logging.Logger: A logger instance configured with the INFO log level.
    """
    new_logger = logging.getLogger()  # Create a new logger instance

    new_logger.setLevel(logging.INFO)  # Set the log level to INFO

    return new_logger  # Return the configured logger instance
