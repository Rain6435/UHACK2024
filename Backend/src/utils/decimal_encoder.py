# Expertus, an IBM Company Confidential
# © Expertus, an IBM Company 2018, 2022, 2023
import decimal
import json

from datetime import date, datetime
from enum import Enum


import utils.date as lib_date


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        elif isinstance(o, datetime) or isinstance(o, date):
            return lib_date.format_datetime(o)
        elif isinstance(o, Enum):
            return o.name
        elif isinstance(o, set):
            return list(o)
        elif isinstance(o, bytes):
            return o.decode("utf-8")
        return super(DecimalEncoder, self).default(o)
