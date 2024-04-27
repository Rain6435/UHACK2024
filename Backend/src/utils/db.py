import mysql.connector

cnx = mysql.connector.connect(host="localhost", user="root", password="", database="uhack2024")
cursor = cnx.cursor()

def get_team_by_id(id):
    cursor.execute(f"SELECT id, name, password, work_time, work_season, secteur, is_admin FROM team WHERE id = {id}")
    team = cursor.fetchall()
    team = team[0] if len(team) > 0 else None
    cursor.execute(f"SELECT id, location_id, team_id, is_dangerous, creation_date, lead_time, fix_date, status, image_path, requestor_id FROM request WHERE team_id = {team[0]}")
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
            'location_id': req[1], 
            'team_id': req[2], 
            'is_dangerous': bool(req[3]),
            'creation_date': req[4],
            'lead_time': req[5],
            'fix_date': req[6],
            "status": req[7],
            "image_path": req[8],
            "requestor_id": req[9],
        } for req in reqs]
    }

def get_all_teams():
    cursor.execute(f"SELECT id, name, password, work_time, work_season, secteur, is_admin FROM team")
    teams = cursor.fetchall()
    ret = []
    for team in teams:
        cursor.execute(f"SELECT id, location_id, team_id, is_dangerous, creation_date, lead_time, fix_date, status, image_path, requestor_id FROM request WHERE team_id = {team[0]}")
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
                'location_id': req[1], 
                'team_id': req[2], 
                'is_dangerous': bool(req[3]),
                'creation_date': req[4],
                'lead_time': req[5],
                'fix_date': req[6],
                "status": req[7],
                "image_path": req[8],
                "requestor_id": req[9],
            } for req in reqs]
        })
        
    return ret

def get_request_id(id):
    cursor.execute(f"SELECT id, location_id, team_id, is_dangerous, creation_date, lead_time, fix_date, status, image_path, requestor_id FROM request WHERE id = {id}")
    req = cursor.fetchall()
    req = req[0] if len(req) > 0 else None

    return {
        'id': req[0], 
        'location_id': req[1], 
        'team_id': req[2], 
        'is_dangerous': bool(req[3]),
        'creation_date': req[4],
        'lead_time': req[5],
        'fix_date': req[6],
        "status": req[7],
        "image_path": req[8],
        "requestor_id": req[9],
    }

def get_all_requests():
    cursor.execute(f"SELECT id, location_id, team_id, is_dangerous, creation_date, lead_time, fix_date, status, image_path, requestor_id FROM request")
    reqs = cursor.fetchall()
    return [{
                'id': req[0], 
                'location_id': req[1], 
                'team_id': req[2], 
                'is_dangerous': bool(req[3]),
                'creation_date': req[4],
                'lead_time': req[5],
                'fix_date': req[6],
                "status": req[7],
                "image_path": req[8],
                "requestor_id": req[9],
    } for req in reqs]

def insert_request(location_id, team_id, is_dangerous, creation_date, lead_time, fix_date, status, image_path, requestor_id):
    cursor.execute(f"INSERT INTO request (location_id, team_id, is_dangerous, creation_date, lead_time, fix_date, status, image_path, requestor_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (location_id, team_id, is_dangerous, creation_date, lead_time, fix_date, status, image_path, requestor_id))
    cnx.commit()
    
    return cursor.lastrowid
