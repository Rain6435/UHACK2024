import pandas as pd
import json
from flask import Response, abort

from utils.api_wrapper import (return_error_response, HTTP_CODE_FORBIDDEN, HTTP_CODE_UNAUTHORIZED, MIME_TYPE_JSON)
from utils.db import (
    get_requestor_by_id,
    get_all_requestor,
    get_requestor_by_name_and_address,
    get_requestor_by_tel,
    get_requestor_by_name_and_tel,
    insert_requestor,
    modify_requestor,
)
from utils.csv_util import get_voie_routier
from utils.date import get_utc_now
from utils.basic import format_tel, format_name

def get_requestors(request):
    id = request.args.get("id", None)

    if id:
        return get_requestor_by_id(id)
    else:           
        return get_all_requestor()

def login_requestor(request):
    body = request.json

    firstname = format_name(body.get('firstname'))
    lastname = format_name(body.get('lastname'))
    tel = format_tel(body.get('tel'))

    print(firstname, lastname, tel)

    if tel and firstname and lastname:
        user = get_requestor_by_name_and_tel(firstname=firstname, lastname=lastname, tel=tel)
    else:
        abort(Response(return_error_response('ERR_GENERAL_E001', 'INVALID'), HTTP_CODE_UNAUTHORIZED, content_type=MIME_TYPE_JSON))
    if not user:
        abort(Response(return_error_response('ERR_GENERAL_E001', 'INVALID'), HTTP_CODE_UNAUTHORIZED, content_type=MIME_TYPE_JSON))

    return user

def create_requestor(request):
    body = request.json
    firstname = format_name(body.get("firstname"))
    lastname = format_name(body.get("lastname"))
    tel = format_tel(body.get("tel"))
    email = body.get("email")
    adresse = body.get("adresse")
    id = body.get("id")
    

    if request.method == "POST":
        requestor_id = insert_requestor(firstname=firstname, lastname=lastname, tel=tel, email=email, adresse=adresse)
    elif id:
        requestor_id = modify_requestor(id=id, firstname=firstname, lastname=lastname, tel=tel, email=email, adresse=adresse)
    else:
        abort(Response(return_error_response('ERR_GENERAL_E001', 'INVALID id'), HTTP_CODE_UNAUTHORIZED, content_type=MIME_TYPE_JSON))

    return requestor_id

    
def delete_requestor(request):
    return ""
