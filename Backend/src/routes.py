from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin

from utils.api_wrapper import (
    return_success_response, 
    create_cors_enabled_app,
    HTTP_CODE_OK, 
    HTTP_CODE_CREATED, 
    HTTP_CODE_NO_CONTENT,
    MIME_TYPE_JSON
)
import teams
import requestors
import _requests

app = create_cors_enabled_app(__name__)


# HTTP Methode
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

@app.route(V1+HEALTH, methods=[GET])
def get_health():
    return app.response_class(response=return_success_response('operational'), status=HTTP_CODE_OK, mimetype=MIME_TYPE_JSON)

# Algo

@app.route(V1+REQUESTS_ROUTE+"/distribute", methods=[PUT])
def calculate_algo():
    return app.response_class(response=return_success_response(_requests.distribute_tasks(request)), status=HTTP_CODE_OK, mimetype=MIME_TYPE_JSON)

# Teams

@app.route(V1+TEAMS_ROUTE, methods=[GET])
def get_teams():
    return app.response_class(response=return_success_response(teams.get_teams(request)), status=HTTP_CODE_OK, mimetype=MIME_TYPE_JSON)

@app.route(V1+TEAMS_ROUTE, methods=[PUT, POST])
def post_teams():
    return app.response_class(response=return_success_response(teams.create_team(request)), status=HTTP_CODE_CREATED, mimetype=MIME_TYPE_JSON)

@app.route(V1+TEAMS_ROUTE+LOGIN, methods=[POST])
def login_team():
    return app.response_class(response=return_success_response(teams.login_team(request)), status=HTTP_CODE_OK, mimetype=MIME_TYPE_JSON)

@app.route(V1+TEAMS_ROUTE, methods=[DELETE])
def delete_teams():
    return app.response_class(response=return_success_response(teams.delete_team(request)), status=HTTP_CODE_NO_CONTENT, mimetype=MIME_TYPE_JSON)

# Requestor

@app.route(V1+REQUESTORS_ROUTE, methods=[GET])
def get_requestors():
    return app.response_class(response=return_success_response(requestors.get_requestors(request)), status=HTTP_CODE_OK, mimetype=MIME_TYPE_JSON)

@app.route(V1+REQUESTORS_ROUTE, methods=[PUT, POST])
def post_requestors():
    return app.response_class(response=return_success_response(requestors.create_requestor(request)), status=HTTP_CODE_CREATED, mimetype=MIME_TYPE_JSON)

@app.route(V1+REQUESTORS_ROUTE+ LOGIN, methods=[POST])
def login_requestors():
    return app.response_class(response=return_success_response(requestors.login_requestor(request)), status=HTTP_CODE_OK, mimetype=MIME_TYPE_JSON)

@app.route(V1+REQUESTORS_ROUTE, methods=[DELETE])
def delete_requestors():
    return app.response_class(response=return_success_response(requestors.delete_requestor(request)), status=HTTP_CODE_NO_CONTENT, mimetype=MIME_TYPE_JSON)

# Request

@app.route(V1+REQUESTS_ROUTE, methods=[GET])
def get_request():
    return app.response_class(response=return_success_response(_requests.get_requests(request)), status=HTTP_CODE_OK, mimetype=MIME_TYPE_JSON)

@app.route(V1+REQUESTS_ROUTE, methods=[PUT, POST])
def post_request():
    return app.response_class(response=return_success_response(_requests.create_request(request)), status=HTTP_CODE_CREATED, mimetype=MIME_TYPE_JSON)

@app.route(V1+REQUESTS_ROUTE, methods=[DELETE])
def delete_request():
    return app.response_class(response=return_success_response(_requests.delete_request(request)), status=HTTP_CODE_NO_CONTENT, mimetype=MIME_TYPE_JSON)
