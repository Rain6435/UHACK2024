import pendulum as pendulum  # Importing the pendulum library for date and time manipulation
import datetime as datetime  # Importing the datetime module for datetime operations

import utils.common as lib_common  # Importing a custom utility module for common functions

LOGGER = lib_common.get_logger()  # Initializing a logger instance


def format_datetime(date_time: datetime.datetime, dt_format=None):
    """
    Converts a datetime object to a string formatted according to the specified format.

    Parameters:
        date_time (datetime.datetime): The datetime object to format.
        dt_format (str): The format string to use for formatting the datetime object.

    Returns:
        str: The formatted datetime string.
    """
    return (
        date_time.strftime(dt_format)
        if dt_format is not None
        else date_time.isoformat()
    )


def get_utc_now(dt_format=None, use_str_result_type=True):
    """
    Gets the current UTC datetime.

    Parameters:
        dt_format (str): The format string to use for formatting the datetime object.
        use_str_result_type (bool): Indicates whether the result should be returned as a string.

    Returns:
        datetime.datetime or str: The current UTC datetime, optionally formatted as a string.
    """
    return get_timezone_now(
        pendulum.UTC, dt_format=dt_format, use_str_result_type=use_str_result_type
    )


def get_timezone_now(timezone, dt_format=None, use_str_result_type=True):
    """
    Gets the current datetime in the specified timezone.

    Parameters:
        timezone: The timezone to use.
        dt_format (str): The format string to use for formatting the datetime object.
        use_str_result_type (bool): Indicates whether the result should be returned as a string.

    Returns:
        datetime.datetime or str: The current datetime in the specified timezone,
                                  optionally formatted as a string.
    """
    time_now = pendulum.now(timezone)  # Get current datetime in the specified timezone

    if not use_str_result_type:
        return time_now

    return format_datetime(time_now, dt_format)


def convert_utc_string_to_datetime(utc_string):
    """
    Converts a UTC datetime string to a datetime object.

    Parameters:
        utc_string (str): The UTC datetime string to convert.

    Returns:
        datetime.datetime or None: The converted datetime object, or None if conversion fails.
    """
    try:
        return pendulum.parse(utc_string, tz="UTC")  # Parse the UTC datetime string
    except ValueError as e:
        LOGGER.info(f"convert_utc_string_to_datetime: Error: {e}")  # Log any errors
        return None
