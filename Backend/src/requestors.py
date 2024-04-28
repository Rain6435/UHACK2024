import pandas as pd
import json
from flask import Response, abort

from utils.api_wrapper import (return_error_response, HTTP_CODE_FORBIDDEN, HTTP_CODE_UNAUTHORIZED, MIME_TYPE_JSON)
from utils.db import (
    get_requestor_by_id,
    get_all_requestor,
    get_requestor_by_name_and_address,
    get_requestor_by_tel,
    get_requestor_by_name_and_tel
)
from utils.csv_util import get_voie_routier
from utils.date import get_utc_now

def get_requestors(request):
    id = request.args.get("id", None)

    if id:
        return get_requestor_by_id(id)
    else:           
        return get_all_requestor()

def login_requestor(request):
    body = request.json

    firstname = body.get('userFname')
    lastname = body.get('userLname')
    adresse = body.get('adresse')
    tel = body.get('telephone')

    if tel and firstname and lastname:
        user = get_requestor_by_name_and_tel(firstname=firstname, lastname=lastname, tel=tel)
    else:
        abort(Response(return_error_response('ERR_GENERAL_E001', 'INVALID'), HTTP_CODE_UNAUTHORIZED, content_type=MIME_TYPE_JSON))
    if not user:
        abort(Response(return_error_response('ERR_GENERAL_E001', 'INVALID'), HTTP_CODE_UNAUTHORIZED, content_type=MIME_TYPE_JSON))

    return user

def create_requestor(request):
    return ""
    
def delete_requestor(request):
    return ""
