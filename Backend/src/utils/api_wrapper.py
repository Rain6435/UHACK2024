# Expertus, an IBM Company Confidential
# © Expertus, an IBM Company 2018, 2022, 2023
import json
import uuid
import os
from typing import Optional

from flask import Blueprint, Flask

import utils.date as lib_date
import utils.decimal_encoder as decimal_encoder

MIME_TYPE_JSON = 'application/json'
MIME_TYPE_TEXT = 'text/plain'

def create_cors_enabled_app(name, blueprint_name=None):
    if blueprint_name is not None:
        app = Blueprint(blueprint_name, name)
    else:
        app = Flask(name)

    @app.after_request
    def add_cors_headers(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        response.headers['Access-Control-Allow-Methods'] = '*'
        return response

    return app


def return_success_response(content, description: Optional[str] = None):
    return json.dumps({
            "response_id": str(uuid.uuid4()),
            "date_utc": lib_date.get_utc_now(),
            "payload": content,
            "description": description,
        }, cls=decimal_encoder.DecimalEncoder)


def return_error_response(error_code, error_message, tag_generic='code', tag_specific='message'):
    return json.dumps({
        "response_id": str(uuid.uuid4()),
        "date_utc": lib_date.get_utc_now(),
        "error": {
            tag_generic: error_code,
            tag_specific: error_message
        }
    }, cls=decimal_encoder.DecimalEncoder)


# OK
# Successful.
HTTP_CODE_OK = 200

# Created
# Created.
HTTP_CODE_CREATED = 201

# No Content
# The server has fulfilled the request but does not need to return an entity-body.
HTTP_CODE_NO_CONTENT = 204

# Miscellaneous Persistent Warning
# The warning text can include arbitrary information to be presented to a human user or logged.  A system receiving this warning MUST NOT
# take any automated action.
HTTP_MISC_PERSISTENT_WARNING = 299

# Bad Request
# Bad input parameter. Error message should indicate which one and why.
HTTP_CODE_BAD_REQUEST = 400

# Unauthorized
# The client passed in the invalid Auth token. Client should refresh the token and then try again.
HTTP_CODE_UNAUTHORIZED = 401

# Forbidden
# Customer does not exist. Application not registered. Application try to access to properties not belong to an App. Application try to trash/purge root node.
# Application try to update contentProperties. Operation is blocked (for third-party apps). Customer account over quota.
HTTP_CODE_FORBIDDEN = 403

# Not Found
# Resource not found.
HTTP_CODE_NOT_FOUND = 404

# Method Not Allowed
# The resource doesn't support the specified HTTP verb.
HTTP_CODE_METHOD_NOT_ALLOWED = 405

# Conflict
# Conflict.
HTTP_CODE_CONFLICT = 409

# Gone
# Access to the target resource is no longer available at the origin server and this condition is likely to be permanent.
HTTP_GONE = 410

# Length Required
# The Content-Length header was not specified.
HTTP_CODE_LENGTH_REQUIRED = 411

# Precondition Failed
# Precondition failed.
HTTP_CODE_PRECONDITION_FAILED = 412

# Too Many Requests
# Too many request for rate limiting.
HTTP_CODE_TOO_MANY_REQUESTS = 429

# Internal Server Error
# Servers are not working as expected. The request is probably valid but needs to be requested again later.
HTTP_CODE_INTERNAL_SERVER_ERROR = 500

# Service Unavailable
# Service Unavailable.
HTTP_CODE_SERVICE_UNAVAILABLE = 503

# Gateway Timeout
# Indicates that the server, while acting as a gateway or proxy, did not get a response in time from the upstream server that it needed in order to complete
# the request.
HTTP_CODE_GATEWAY_TIMEOUT = 504

