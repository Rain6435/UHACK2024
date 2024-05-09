from flask import request

from utils.api_wrapper import (
    return_success_response,
    create_cors_enabled_app,
    HTTP_CODE_OK,
    HTTP_CODE_CREATED,
    HTTP_CODE_NO_CONTENT,
    MIME_TYPE_JSON,
)
import teams
import requestors
import _requests

# Create a Flask app with CORS enabled
app = create_cors_enabled_app(__name__)

# Constants for HTTP methods
GET = "GET"
POST = "POST"
PUT = "PUT"
DELETE = "DELETE"

# Routes
V1 = "/v1"
LOGIN = "/login"
HEALTH = "/health"
TEAMS_ROUTE = "/teams"
REQUESTORS_ROUTE = "/users"
REQUESTS_ROUTE = "/requests"


@app.route(V1 + HEALTH, methods=[GET])
def get_health():
    """
    Endpoint to check the health of the application.

    Returns:
        Response indicating the operational status.
    """
    return app.response_class(
        response=return_success_response("operational"),
        status=HTTP_CODE_OK,
        mimetype=MIME_TYPE_JSON,
    )


# Algo
@app.route(V1 + REQUESTS_ROUTE + "/distribute", methods=[PUT])
def calculate_algo():
    """
    Endpoint to calculate the algorithm for distributing tasks.

    Returns:
        Response indicating the success of the algorithm calculation.
    """
    return app.response_class(
        response=return_success_response(_requests.distribute_tasks(request)),
        status=HTTP_CODE_OK,
        mimetype=MIME_TYPE_JSON,
    )


# Teams
@app.route(V1 + TEAMS_ROUTE, methods=[GET])
def get_teams():
    """
    Endpoint to retrieve all teams.

    Returns:
        Response containing the list of teams.
    """
    return app.response_class(
        response=return_success_response(teams.get_teams(request)),
        status=HTTP_CODE_OK,
        mimetype=MIME_TYPE_JSON,
    )


@app.route(V1 + TEAMS_ROUTE, methods=[PUT, POST])
def post_teams():
    """
    Endpoint to create or modify a team.

    Returns:
        Response indicating the success of the team creation or modification.
    """
    return app.response_class(
        response=return_success_response(teams.create_team(request)),
        status=HTTP_CODE_CREATED,
        mimetype=MIME_TYPE_JSON,
    )


@app.route(V1 + TEAMS_ROUTE + LOGIN, methods=[POST])
def login_team():
    """
    Endpoint for team login.

    Returns:
        Response containing the login status of the team.
    """
    return app.response_class(
        response=return_success_response(teams.login_team(request)),
        status=HTTP_CODE_OK,
        mimetype=MIME_TYPE_JSON,
    )


@app.route(V1 + TEAMS_ROUTE, methods=[DELETE])
def delete_teams():
    """
    Endpoint to delete a team.

    Returns:
        Response indicating the success of the team deletion.
    """
    return app.response_class(
        response=return_success_response(teams.delete_team(request)),
        status=HTTP_CODE_NO_CONTENT,
        mimetype=MIME_TYPE_JSON,
    )


# Requestor
@app.route(V1 + REQUESTORS_ROUTE, methods=[GET])
def get_requestors():
    """
    Endpoint to retrieve all requestors.

    Returns:
        Response containing the list of requestors.
    """
    return app.response_class(
        response=return_success_response(requestors.get_requestors(request)),
        status=HTTP_CODE_OK,
        mimetype=MIME_TYPE_JSON,
    )


@app.route(V1 + REQUESTORS_ROUTE, methods=[PUT, POST])
def post_requestors():
    """
    Endpoint to create or modify a requestor.

    Returns:
        Response indicating the success of the requestor creation or modification.
    """
    return app.response_class(
        response=return_success_response(requestors.create_requestor(request)),
        status=HTTP_CODE_CREATED,
        mimetype=MIME_TYPE_JSON,
    )


@app.route(V1 + REQUESTORS_ROUTE + LOGIN, methods=[POST])
def login_requestors():
    """
    Endpoint for requestor login.

    Returns:
        Response containing the login status of the requestor.
    """
    return app.response_class(
        response=return_success_response(requestors.login_requestor(request)),
        status=HTTP_CODE_OK,
        mimetype=MIME_TYPE_JSON,
    )


@app.route(V1 + REQUESTORS_ROUTE, methods=[DELETE])
def delete_requestors():
    """
    Endpoint to delete a requestor.

    Returns:
        Response indicating the success of the requestor deletion.
    """
    return app.response_class(
        response=return_success_response(requestors.delete_requestor(request)),
        status=HTTP_CODE_NO_CONTENT,
        mimetype=MIME_TYPE_JSON,
    )


# Request
@app.route(V1 + REQUESTS_ROUTE, methods=[GET])
def get_request():
    """
    Endpoint to retrieve all requests.

    Returns:
        Response containing the list of requests.
    """
    return app.response_class(
        response=return_success_response(_requests.get_requests(request)),
        status=HTTP_CODE_OK,
        mimetype=MIME_TYPE_JSON,
    )


@app.route(V1 + REQUESTS_ROUTE, methods=[PUT, POST])
def post_request():
    """
    Endpoint to create or modify a request.

    Returns:
        Response indicating the success of the request creation or modification.
    """
    return app.response_class(
        response=return_success_response(_requests.create_request(request)),
        status=HTTP_CODE_CREATED,
        mimetype=MIME_TYPE_JSON,
    )


@app.route(V1 + REQUESTS_ROUTE, methods=[DELETE])
def delete_request():
    """
    Endpoint to delete a request.

    Returns:
        Response indicating the success of the request deletion.
    """
    return app.response_class(
        response=return_success_response(_requests.delete_request(request)),
        status=HTTP_CODE_NO_CONTENT,
        mimetype=MIME_TYPE_JSON,
    )
