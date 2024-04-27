import mysql.connector
import json

cnx = mysql.connector.connect(host="localhost", user="root", password="", database="uhack2024")
cursor = cnx.cursor()

def get_team_by_id(id):
    cursor.execute(f"SELECT id, name, password, work_time, work_season, secteur, is_admin FROM team WHERE id = {id}")
    team = cursor.fetchall()
    team = team[0] if len(team) > 0 else None
    cursor.execute(f"SELECT id, location, team_id, is_dangerous, creation_date, lead_time, fix_date, status, image, requestor_id FROM request WHERE team_id = {team[0]}")
    reqs = cursor.fetchall()
    return {
        'info': {
            'id': team[0],
            'name': team[1],
            'password': team[2],
            'work_time': team[3],
            'work_season': team[4],
            'secteur': team[5],
            'is_admin': team[6],
        },
        'requests': [{
            'id': req[0], 
            'location': json.loads(req[1]), 
            'team_id': req[2], 
            'is_dangerous': bool(req[3]),
            'creation_date': req[4],
            'lead_time': req[5],
            'fix_date': req[6],
            "status": req[7],
            "image": req[8],
            "requestor_id": req[9],
        } for req in reqs]
    }

def get_all_teams():
    cursor.execute(f"SELECT id, name, password, work_time, work_season, secteur, is_admin FROM team")
    teams = cursor.fetchall()
    ret = []
    for team in teams:
        cursor.execute(f"SELECT id, location, team_id, is_dangerous, creation_date, lead_time, fix_date, status, image, requestor_id FROM request WHERE team_id = {team[0]}")
        reqs = cursor.fetchall()

        ret.append({
            'info': {
                'id': team[0],
                'name': team[1],
                'password': team[2],
                'work_time': team[3],
                'work_season': team[4],
                'secteur': team[5],
                'is_admin': team[6],
            },
            'requests': [{
                'id': req[0], 
                'location': json.loads(req[1]), 
                'team_id': req[2], 
                'is_dangerous': bool(req[3]),
                'creation_date': req[4],
                'lead_time': req[5],
                'fix_date': req[6],
                "status": req[7],
                "image": req[8],
                "requestor_id": req[9],
            } for req in reqs]
        })
        
    return ret

def get_request_id(id):
    cursor.execute(f"SELECT id, location, team_id, is_dangerous, creation_date, lead_time, fix_date, status, image, requestor_id FROM request WHERE id = {id}")
    req = cursor.fetchall()
    req = req[0] if len(req) > 0 else None

    return {
        'id': req[0], 
        'location': json.loads(req[1]), 
        'team_id': req[2], 
        'is_dangerous': bool(req[3]),
        'creation_date': req[4],
        'lead_time': req[5],
        'fix_date': req[6],
        "status": req[7],
        "image": req[8],
        "requestor_id": req[9],
    } if req else None

def get_all_requests():
    cursor.execute(f"SELECT id, location, team_id, is_dangerous, creation_date, lead_time, fix_date, status, image, requestor_id FROM request")
    reqs = cursor.fetchall()
    return [{
                'id': req[0], 
                'location': json.loads(req[1]), 
                'team_id': req[2], 
                'is_dangerous': bool(req[3]),
                'creation_date': req[4],
                'lead_time': req[5],
                'fix_date': req[6],
                "status": req[7],
                "image": req[8],
                "requestor_id": req[9],
    } for req in reqs]

def insert_request(location, is_dangerous, creation_date, adresse, status, image, requestor_id, team_id=None, lead_time=None, fix_date=None):
    cursor = cnx.cursor()
    cursor.execute(f"INSERT INTO request (location, team_id, is_dangerous, creation_date, adresse, lead_time, fix_date, status, image, requestor_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (location, team_id, is_dangerous, creation_date, adresse, lead_time, fix_date, status, image, requestor_id))
    cnx.commit()
    cursor.close()
    
    return cursor.lastrowid

def get_requestor_by_tel(tel):
    cursor = cnx.cursor()
    cursor.execute(f"SELECT id, firstname, lastname, adresse, email, tel FROM requestor WHERE tel = '{tel}'")
    user = cursor.fetchall()
    user = user[0] if len(user) > 0 else None
    cursor.close()
    
    return {
        'id': user[0], 
        'firstname': user[1], 
        'lastname': user[2], 
        'adresse': user[3],
        'email': user[4],
        'tel': user[5]
    } if user else None

def get_requestor_by_name_and_address(firstname, lastname, adresse):
    cursor = cnx.cursor()
    cursor.execute(f"SELECT id, firstname, lastname, adresse, email, tel FROM requestor WHERE firstname = '{firstname}' AND lastname = '{lastname}' AND adresse = '{adresse}'")
    user = cursor.fetchall()
    user = user[0] if len(user) > 0 else None
    cursor.close()
    
    return {
        'id': user[0], 
        'firstname': user[1], 
        'lastname': user[2], 
        'adresse': user[3],
        'email': user[4],
        'tel': user[5]
    } if user else None

def get_requestor_by_email(email):
    cursor = cnx.cursor()
    cursor.execute(f"SELECT id, firstname, lastname, adresse, email, tel FROM requestor WHERE email = '{email}'")
    user = cursor.fetchall()
    user = user[0] if len(user) > 0 else None
    cursor.close()
    
    return {
        'id': user[0], 
        'firstname': user[1], 
        'lastname': user[2], 
        'adresse': user[3],
        'email': user[4],
        'tel': user[5]
    }

def insert_requestor(firstname, lastname, email, tel, adresse=None,):
    cursor = cnx.cursor()
    cursor.execute("INSERT INTO requestor (firstname, lastname, adresse, email, tel) VALUES (%s, %s, %s, %s, %s)", (firstname, lastname, adresse, email, tel))
    cnx.commit()
    last_insert_id = cursor.lastrowid
    cursor.close()
    
    return last_insert_id