import json  # Importing the json module for JSON serialization and deserialization
import uuid  # Importing the uuid module for generating universally unique identifiers
from typing import Optional  # Importing the Optional type from the typing module

from flask import (
    Blueprint,
    Flask,
)  # Importing Flask and Blueprint from the Flask framework

import utils.date as lib_date  # Importing a custom utility module for date-related functions
import utils.decimal_encoder as decimal_encoder  # Importing a custom JSON encoder module for handling decimal objects


MIME_TYPE_JSON = "application/json"  # Constant representing the JSON MIME type
MIME_TYPE_TEXT = "text/plain"  # Constant representing the plain text MIME type


def create_cors_enabled_app(name, blueprint_name=None):
    """
    Creates a Flask application with CORS (Cross-Origin Resource Sharing) enabled.

    Parameters:
        name (str): The name of the Flask application.
        blueprint_name (str): The name of the blueprint, if applicable.

    Returns:
        Flask or Blueprint: The Flask application instance or blueprint with CORS enabled.
    """
    if blueprint_name is not None:
        app = Blueprint(
            blueprint_name, name
        )  # Create a blueprint if a blueprint name is provided
    else:
        app = Flask(name)  # Otherwise, create a regular Flask application

    @app.after_request
    def add_cors_headers(response):
        """
        Adds CORS headers to the response.

        Parameters:
            response (Flask.Response): The Flask response object.

        Returns:
            Flask.Response: The modified Flask response object with CORS headers.
        """
        response.headers["Access-Control-Allow-Origin"] = (
            "*"  # Allow requests from any origin
        )
        response.headers["Access-Control-Allow-Headers"] = (
            "Content-Type"  # Allow the Content-Type header
        )
        response.headers["Access-Control-Allow-Methods"] = "*"  # Allow all HTTP methods
        return response

    return app


def return_success_response(content, description: Optional[str] = None):
    """
    Returns a successful JSON response with the provided content.

    Parameters:
        content: The payload content of the response.
        description (str, optional): A description of the response.

    Returns:
        str: A JSON-formatted success response.
    """
    return json.dumps(
        {
            "response_id": str(uuid.uuid4()),  # Generate a unique response ID
            "date_utc": lib_date.get_utc_now(),  # Get the current UTC date and time
            "payload": content,  # Set the payload content
            "description": description,  # Set the response description
        },
        cls=decimal_encoder.DecimalEncoder,  # Use the custom decimal encoder for serialization
    )


def return_error_response(
    error_code, error_message, tag_generic="code", tag_specific="message"
):
    """
    Returns an error JSON response with the provided error code and message.

    Parameters:
        error_code: The error code to indicate the type of error.
        error_message: The error message describing the error.
        tag_generic (str): The tag name for the generic error information.
        tag_specific (str): The tag name for the specific error message.

    Returns:
        str: A JSON-formatted error response.
    """
    return json.dumps(
        {
            "response_id": str(uuid.uuid4()),  # Generate a unique response ID
            "date_utc": lib_date.get_utc_now(),  # Get the current UTC date and time
            "error": {
                tag_generic: error_code,
                tag_specific: error_message,
            },  # Set the error information
        },
        cls=decimal_encoder.DecimalEncoder,  # Use the custom decimal encoder for serialization
    )


# HTTP Status Codes

# OK
HTTP_CODE_OK = 200

# Created
HTTP_CODE_CREATED = 201

# No Content
HTTP_CODE_NO_CONTENT = 204

# Miscellaneous Persistent Warning
HTTP_MISC_PERSISTENT_WARNING = 299

# Bad Request
HTTP_CODE_BAD_REQUEST = 400

# Unauthorized
HTTP_CODE_UNAUTHORIZED = 401

# Forbidden
HTTP_CODE_FORBIDDEN = 403

# Not Found
HTTP_CODE_NOT_FOUND = 404

# Method Not Allowed
HTTP_CODE_METHOD_NOT_ALLOWED = 405

# Conflict
HTTP_CODE_CONFLICT = 409

# Gone
HTTP_GONE = 410

# Length Required
HTTP_CODE_LENGTH_REQUIRED = 411

# Precondition Failed
HTTP_CODE_PRECONDITION_FAILED = 412

# Too Many Requests
HTTP_CODE_TOO_MANY_REQUESTS = 429

# Internal Server Error
HTTP_CODE_INTERNAL_SERVER_ERROR = 500

# Service Unavailable
HTTP_CODE_SERVICE_UNAVAILABLE = 503

# Gateway Timeout
HTTP_CODE_GATEWAY_TIMEOUT = 504
