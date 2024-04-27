import pendulum as pendulum
import datetime as datetime

import utils.common as lib_common

LOGGER = lib_common.get_logger()


# Datetime to str
def format_datetime(date_time: datetime.datetime, dt_format=None):
    return date_time.strftime(dt_format) if dt_format is not None else date_time.isoformat()


def get_utc_now(dt_format=None, use_str_result_type=True):
    return get_timezone_now(pendulum.UTC, dt_format=dt_format, use_str_result_type=use_str_result_type)


def get_timezone_now(timezone, dt_format=None, use_str_result_type=True):
    time_now = pendulum.now(timezone)

    if not use_str_result_type:
        return time_now

    return format_datetime(time_now, dt_format)

def convert_utc_string_to_datetime(utc_string):
    try:
        return pendulum.parse(utc_string, tz="UTC")
    except ValueError as e:
        LOGGER.info(f"convert_utc_string_to_datetime: Error: {e}")
        return None
