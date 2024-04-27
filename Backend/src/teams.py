import mysql.connector
from utils.db import get_team_by_id, get_all_teams
from flask import Response, abort
from utils.api_wrapper import (return_error_response, HTTP_CODE_FORBIDDEN, HTTP_CODE_UNAUTHORIZED, MIME_TYPE_JSON)

cnx = mysql.connector.connect(host="localhost", user="root", password="", database="uhack2024")
cursor = cnx.cursor()

def get_teams(request):
    id = request.args.get("id", None)

    if id:
        return get_team_by_id(id)
    else:           
        return get_all_teams()

def create_team(request):
    return ""

def delete_team(request):
    return ""

def login_team(request):
    id = request.args.get("id", None)

    print("id", id)

    if not id:
        abort(Response(return_error_response("ERR_GENERAL_E001", "Missing id"), HTTP_CODE_FORBIDDEN, content_type=MIME_TYPE_JSON))

    team = get_team_by_id(id)

    if not team:
        abort(Response(return_error_response("ERR_GENERAL_E001", "Invalid"), HTTP_CODE_FORBIDDEN, content_type=MIME_TYPE_JSON))

    return team