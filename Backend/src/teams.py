import mysql.connector
from utils.db import get_team_by_id, get_all_teams

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
    return ""