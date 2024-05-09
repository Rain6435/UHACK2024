import decimal  # Importing the decimal module for decimal arithmetic
import json  # Importing the json module for JSON serialization and deserialization

from datetime import (
    date,
    datetime,
)  # Importing date and datetime classes from the datetime module
from enum import Enum  # Importing the Enum class for creating enumerated types

import utils.date as lib_date  # Importing a custom utility module for date formatting


class DecimalEncoder(json.JSONEncoder):
    """Custom JSON encoder class for handling special types during JSON serialization."""

    def default(self, o):
        """Overrides the default method to customize JSON serialization behavior."""
        if isinstance(o, decimal.Decimal):  # If object is a decimal.Decimal
            if o % 1 > 0:  # If it has a fractional part
                return float(o)  # Convert to float
            else:
                return int(o)  # Convert to integer
        elif isinstance(o, datetime) or isinstance(
            o, date
        ):  # If object is a datetime or date
            return lib_date.format_datetime(
                o
            )  # Format using custom date formatting function
        elif isinstance(o, Enum):  # If object is an Enum
            return o.name  # Return the name of the Enum
        elif isinstance(o, set):  # If object is a set
            return list(o)  # Convert to list
        elif isinstance(o, bytes):  # If object is bytes
            return o.decode("utf-8")  # Decode from UTF-8 to string
        return super(DecimalEncoder, self).default(
            o
        )  # For other types, use default serialization
