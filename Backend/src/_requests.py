import pandas as pd
import json

from utils.db import get_all_requests, get_request_id, insert_request
from utils.csv_util import get_voie_routier


def get_requests(request):
    id = request.args.get("id", None)

    df = get_voie_routier()
    location = df[df['CODEID'] == int(id)]
    return json.loads(location.to_json(orient='records'))

    if id:
        return get_request_id(id)
    else:           
        return get_all_requests()

def create_request(request):
    body = request.json
    
    adresse = body.get('adresse')

    # Find location_id
    df = get_voie_routier()
    location = df[df['CODEID'] == id]


    if (request.method == "POST"):
        req_id = insert_request(
            body.get('location_id'), 
            body.get('team_id'), 
            body.get('is_dangerous'), 
            body.get('creation_date'), 
            body.get('lead_time'), 
            body.get('fix_date'), 
            body.get('status'), 
            body.get('image_path'), 
            body.get('requestor_id')
        )
    
    return req_id


    
def delete_request(request):
    return ""
