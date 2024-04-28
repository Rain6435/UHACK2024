import pandas as pd
import json
from flask import Response, abort

from utils.api_wrapper import (return_error_response, HTTP_CODE_FORBIDDEN, HTTP_CODE_UNAUTHORIZED, MIME_TYPE_JSON)
from utils.db import (
    get_all_requests, 
    get_request_id, 
    insert_request, 
    get_requestor_by_email, 
    get_requestor_by_name_and_address, 
    get_requestor_by_tel, 
    get_requestor_by_name_and_tel,
    insert_requestor,
    modify_request
)
from utils.csv_util import get_voie_routier
from utils.date import get_utc_now
from utils.basic import format_tel, format_name
from utils.algo import algo

STATUS_PENDING = "PENDING"

def get_requests(request):
    id = request.args.get("id", None)

    if id:
        return get_request_id(id)
    else:           
        return get_all_requests()

def create_request(request):
    body = request.json

    adresse_component = body.get('potholeAddress', {}).get("address_components", [])
    adresse = body.get('potholeAddress', {}).get("formatted_address")
    dangerous = body.get('dangerous')
    image = body.get('image')
    email = body.get('email')
    firstname = format_name(body.get('userFname'))
    lastname = format_name(body.get('userLname'))
    tel = format_tel(body.get('tel'))
    team_id = body.get('team_id')
    lead_time = body.get('lead_time')
    fix_date = body.get('fix_date')
    
    if request.method == "PUT":
        id = body.get("id")
        status = body.get("status")
        req_id = modify_request(id=id, is_dangerous=dangerous, status=status, image=image, team_id=team_id, lead_time=lead_time, fix_date=fix_date)
        return req_id

    route = [a['long_name'] for a in adresse_component if a.get('types')[0] == 'route'][0]
    
    print("route", route)

    # Find location_id
    df = get_voie_routier()
    location = json.loads(df.loc[df['NOM_TOPO'] == route].to_json(orient='records'))
    if not location:
        abort(Response(return_error_response("ERR_GENERAL_E001", "Invalid adresse"), HTTP_CODE_FORBIDDEN, content_type=MIME_TYPE_JSON))
        
    # Add requestor info
    if firstname and lastname and tel:
        requestor = get_requestor_by_name_and_tel(firstname=firstname, lastname=lastname, tel=tel)
    else:
        abort(Response(return_error_response('ERR_GENERAL_E001', 'INVALID missinge firstname, lastname or tel'), HTTP_CODE_UNAUTHORIZED, content_type=MIME_TYPE_JSON))

    if not requestor:
        requestor_id = insert_requestor(firstname=firstname, lastname=lastname, tel=tel, email=email)
    else:
        requestor_id = requestor.get('id')

    if (request.method == "POST"):
        req_id = insert_request(
            location=json.dumps(location[0]), # TODO
            adresse=adresse,
            is_dangerous=bool(dangerous), 
            creation_date=get_utc_now(), 
            status=STATUS_PENDING,
            image=image, 
            requestor_id=requestor_id
        )

        if not req_id:
            abort(Response(return_error_response('ERR_GENERAL_E001', 'NO DUPLICATES'), HTTP_CODE_UNAUTHORIZED, content_type=MIME_TYPE_JSON))
    
    return req_id

    
def delete_request(request):
    return ""

def distribute_tasks(requests):
    # [ids of teams]

    pass