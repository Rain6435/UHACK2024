import pandas as pd
import json
import random
from flask import Response, abort

# Custom imports
from utils.api_wrapper import (
    return_error_response,
    HTTP_CODE_FORBIDDEN,
    HTTP_CODE_UNAUTHORIZED,
    MIME_TYPE_JSON,
)
from utils.db import (
    get_all_requests,
    get_all_requestor,
    get_request_id,
    insert_request,
    get_requestor_by_name_and_tel,
    insert_requestor,
    modify_request,
    get_all_teams,
)
from utils.csv_util import get_voie_routier, get_pothole_test_data
from utils.date import get_utc_now
from utils.basic import format_tel, format_name
from utils.algo import schedule_potholes

STATUS_PENDING = "PENDING"


def get_requests(request):
    """
    Retrieves requests from the database.

    Args:
        request: Flask request object.

    Returns:
        Response: Response containing the requested data.
    """
    id = request.args.get("id", None)

    if id:
        return get_request_id(id)
    else:
        return get_all_requests()


def create_request(request):
    """
    Creates a new request in the database.

    Args:
        request: Flask request object.

    Returns:
        int: ID of the newly created request.
    """
    body = request.json

    # Extract request information from the request body
    adresse_component = body.get("potholeAddress", {}).get("address_components", [])
    adresse = body.get("potholeAddress", {}).get("formatted_address")
    dangerous = body.get("dangerous")
    image = body.get("image")
    email = body.get("email")
    firstname = format_name(body.get("userFname"))
    lastname = format_name(body.get("userLname"))
    tel = format_tel(body.get("tel"))
    team_id = body.get("team_id")
    lead_time = body.get("lead_time")
    fix_date = body.get("fix_date")

    # Handle PUT request for modifying an existing request
    if request.method == "PUT":
        id = body.get("id")
        status = body.get("status")
        req_id = modify_request(
            id=id,
            is_dangerous=dangerous,
            status=status,
            image=image,
            team_id=team_id,
            lead_time=lead_time,
            fix_date=fix_date,
        )
        return req_id

    route = [a["long_name"] for a in adresse_component if a.get("types")[0] == "route"][
        0
    ]

    print("route", route)

    # Find location_id
    df = get_voie_routier()
    location = json.loads(df.loc[df["NOM_TOPO"] == route].to_json(orient="records"))
    if not location:
        abort(
            Response(
                return_error_response("ERR_GENERAL_E001", "Invalid adresse"),
                HTTP_CODE_FORBIDDEN,
                content_type=MIME_TYPE_JSON,
            )
        )

    # Add requestor info
    if firstname and lastname and tel:
        requestor = get_requestor_by_name_and_tel(
            firstname=firstname, lastname=lastname, tel=tel
        )
    else:
        abort(
            Response(
                return_error_response(
                    "ERR_GENERAL_E001", "INVALID missinge firstname, lastname or tel"
                ),
                HTTP_CODE_UNAUTHORIZED,
                content_type=MIME_TYPE_JSON,
            )
        )

    if not requestor:
        requestor_id = insert_requestor(
            firstname=firstname, lastname=lastname, tel=tel, email=email
        )
    else:
        requestor_id = requestor.get("id")

    if request.method == "POST":
        req_id = insert_request(
            location=json.dumps(location[0]),  # TODO
            adresse=adresse,
            is_dangerous=bool(dangerous),
            creation_date=get_utc_now(),
            status=STATUS_PENDING,
            image=image,
            requestor_id=requestor_id,
        )

        if not req_id:
            abort(
                Response(
                    return_error_response("ERR_GENERAL_E001", "NO DUPLICATES"),
                    HTTP_CODE_UNAUTHORIZED,
                    content_type=MIME_TYPE_JSON,
                )
            )

    return req_id


def delete_request(request):
    """
    Deletes a request from the database.

    Args:
        request: Flask request object.

    Returns:
        str: Empty string.
    """
    return ""


def distribute_tasks(requests):
    """
    Distributes tasks among teams based on requests.

    Args:
        requests: List of requests.

    Returns:
        dict: Dictionary containing the distribution of tasks among teams.
    """
    # [ids of teams]
    teams = get_all_teams()
    requestors = get_all_requestor()
    requestors_ids = [requestor.get("info").get("id") for requestor in requestors]
    team_ids = [team.get("info").get("id") for team in teams]

    pothole_test_data = get_pothole_test_data()

    print("id", team_ids)
    print(pothole_test_data)

    out = schedule_potholes(pothole_test_data, team_ids)

    for team_id, pothole_id_obj in out.items():
        print("lvl1", team_id, pothole_id_obj)
        for priority, pothole_data in pothole_id_obj.items():
            print("lvl2", priority, pothole_data)
            location = pothole_data.get("address")
            is_dangerous = pothole_data.get("is_dangerous")
            date = pothole_data.get("date")

            req_id = insert_request(
                location=json.dumps(location),  # TODO
                adresse=location,
                is_dangerous=bool(is_dangerous),
                creation_date=get_utc_now(),
                lead_time=date,
                team_id=team_id,
                status=STATUS_PENDING,
                image="",
                requestor_id=random.choice(requestors_ids),
            )
            print("req_id", req_id)

    return out
