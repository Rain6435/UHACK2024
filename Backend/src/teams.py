import mysql.connector
from flask import Response, abort
from utils.api_wrapper import return_error_response, HTTP_CODE_FORBIDDEN, MIME_TYPE_JSON
from utils.db import get_team_by_id, get_all_teams

# Establish database connection
cnx = mysql.connector.connect(
    host="localhost", user="root", password="", database="uhack2024"
)
cursor = cnx.cursor()


def get_teams(request):
    """
    Retrieves teams based on the provided request.

    Args:
        request: Flask request object.

    Returns:
        Response containing the list of teams or a specific team.
    """
    id = request.args.get("id", None)

    if id:
        return get_team_by_id(id)
    else:
        return get_all_teams()


def create_team(request):
    """
    Creates a new team.

    Args:
        request: Flask request object.

    Returns:
        Response indicating the success of the team creation.
    """
    # Implement transaction
    try:
        cursor.execute("START TRANSACTION")

        # Your team creation logic goes here

        cursor.execute("COMMIT")
        return Response("Team created successfully", status=200)
    except Exception as e:
        cursor.execute("ROLLBACK")
        abort(
            Response(
                return_error_response("ERR_GENERAL_E001", str(e)),
                HTTP_CODE_FORBIDDEN,
                content_type=MIME_TYPE_JSON,
            )
        )


def delete_team(request):
    """
    Deletes a team.

    Args:
        request: Flask request object.

    Returns:
        Response indicating the success of the team deletion.
    """
    # Implement transaction
    try:
        cursor.execute("START TRANSACTION")

        # Your team deletion logic goes here

        cursor.execute("COMMIT")
        return Response("Team deleted successfully", status=200)
    except Exception as e:
        cursor.execute("ROLLBACK")
        abort(
            Response(
                return_error_response("ERR_GENERAL_E001", str(e)),
                HTTP_CODE_FORBIDDEN,
                content_type=MIME_TYPE_JSON,
            )
        )


def login_team(request):
    """
    Logs in a team.

    Args:
        request: Flask request object.

    Returns:
        Response containing the team information if successful, otherwise returns an error response.
    """
    body = request.json
    id = body.get("id", None)

    if not id:
        abort(
            Response(
                return_error_response("ERR_GENERAL_E001", "Missing id"),
                HTTP_CODE_FORBIDDEN,
                content_type=MIME_TYPE_JSON,
            )
        )

    team = get_team_by_id(id)

    if not team:
        abort(
            Response(
                return_error_response("ERR_GENERAL_E001", "Invalid"),
                HTTP_CODE_FORBIDDEN,
                content_type=MIME_TYPE_JSON,
            )
        )

    return team
