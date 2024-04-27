import mysql.connector

cnx = mysql.connector.connect(host="localhost", user="root", password="", database="uhack2024")
cursor = cnx.cursor()

# id = 6
# cursor.execute(f"SELECT id, name, password, work_time, work_season, secteur, is_admin FROM team WHERE id = {id}")
# team = cursor.fetchall()[0]

# print({
#             'id': team[0],
#             'name': team[1],
#             'password': team[2],
#             'work_time': team[3],
#             'work_season': team[4],
#             'secteur': team[5],
#             'is_admin': team[6],
#         })

id = 3
cursor.execute(f"SELECT id, location_id, team_id, is_dangerous, creation_date, lead_time, fix_date, status, image_path, requestor_id FROM request WHERE id = {id}")
req = cursor.fetchall()
req = req if len(req) > 0 else None
print(req)