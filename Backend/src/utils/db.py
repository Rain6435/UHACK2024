import mysql.connector
import json

# Establishing a connection to the MySQL database
cnx = mysql.connector.connect(
    host="localhost",  # MySQL server hostname
    user="root",  # MySQL username
    password="",  # MySQL password
    database="uhack2024",  # Name of the MySQL database
)

# Creating a cursor object to execute SQL queries
cursor = cnx.cursor()


def get_team_by_id(id):
    """
    Retrieves team information and associated requests by team ID from the database.

    Parameters:
        id (int): The ID of the team to retrieve.

    Returns:
        dict or None: A dictionary containing team information and associated requests if the team is found,
                      otherwise None.
    """
    try:
        # Start a transaction
        cnx.start_transaction()

        # Execute the query to fetch team information
        cursor.execute(
            f"SELECT id, name, password, work_time, work_season, secteur, is_admin FROM team WHERE id = {id}"
        )
        team = cursor.fetchall()
        team = team[0] if len(team) > 0 else None

        # Execute the query to fetch requests associated with the team
        cursor.execute(
            f"SELECT id, location, team_id, is_dangerous, creation_date, lead_time, fix_date, status, image, requestor_id, adresse, priority FROM request WHERE team_id = {team[0]}"
        )
        reqs = cursor.fetchall()

        # Commit the transaction
        cnx.commit()

        return (
            {
                "info": {
                    "id": team[0],
                    "name": team[1],
                    "password": team[2],
                    "work_time": team[3],
                    "work_season": team[4],
                    "secteur": team[5],
                    "is_admin": team[6],
                },
                "requests": [
                    {
                        "id": req[0],
                        "location": json.loads(req[1]),
                        "team_id": req[2],
                        "is_dangerous": bool(req[3]),
                        "creation_date": req[4],
                        "lead_time": req[5],
                        "fix_date": req[6],
                        "status": req[7],
                        "image": req[8],
                        "requestor_id": req[9],
                        "adresse": req[10],
                        "priority": req[11],
                    }
                    for req in reqs
                ],
            }
            if team
            else None
        )
    except Exception as e:
        # Rollback the transaction if an error occurs
        cnx.rollback()
        raise e


def get_all_teams():
    """
    Retrieves all teams and their associated requests from the database.

    Returns:
        list: A list of dictionaries, each containing team information and associated requests.
    """
    try:
        # Start a transaction
        cnx.start_transaction()

        # Create a cursor object
        cursor = cnx.cursor()

        # Execute the query to fetch all teams
        cursor.execute(
            f"SELECT id, name, password, work_time, work_season, secteur, is_admin FROM team"
        )
        teams = cursor.fetchall()
        ret = []

        for team in teams:
            # Execute the query to fetch requests associated with each team
            cursor.execute(
                f"SELECT id, location, team_id, is_dangerous, creation_date, lead_time, fix_date, status, image, requestor_id, adresse, priority FROM request WHERE team_id = {team[0]}"
            )
            reqs = cursor.fetchall()

            # Append team information and associated requests to the result list
            ret.append(
                {
                    "info": {
                        "id": team[0],
                        "name": team[1],
                        "password": team[2],
                        "work_time": team[3],
                        "work_season": team[4],
                        "secteur": team[5],
                        "is_admin": team[6],
                    },
                    "requests": [
                        {
                            "id": req[0],
                            "location": json.loads(req[1]),
                            "team_id": req[2],
                            "is_dangerous": bool(req[3]),
                            "creation_date": req[4],
                            "lead_time": req[5],
                            "fix_date": req[6],
                            "status": req[7],
                            "image": req[8],
                            "requestor_id": req[9],
                            "adresse": req[10],
                            "priority": req[11],
                        }
                        for req in reqs
                    ],
                }
            )

        # Commit the transaction
        cnx.commit()

        return ret
    except Exception as e:
        # Rollback the transaction if an error occurs
        cnx.rollback()
        raise e


def get_request_id(id):
    """
    Retrieves a request by its ID from the database.

    Parameters:
        id (int): The ID of the request to retrieve.

    Returns:
        dict or None: A dictionary containing request information if the request is found, otherwise None.
    """
    try:
        # Start a transaction
        cnx.start_transaction()

        # Execute the query to fetch the request by its ID
        cursor.execute(
            f"SELECT id, location, team_id, is_dangerous, creation_date, lead_time, fix_date, status, image, requestor_id, adresse, priority FROM request WHERE id = {id}"
        )
        req = cursor.fetchall()
        req = req[0] if len(req) > 0 else None

        # Commit the transaction
        cnx.commit()

        return (
            {
                "id": req[0],
                "location": json.loads(req[1]),
                "team_id": req[2],
                "is_dangerous": bool(req[3]),
                "creation_date": req[4],
                "lead_time": req[5],
                "fix_date": req[6],
                "status": req[7],
                "image": req[8],
                "requestor_id": req[9],
                "adresse": req[10],
                "priority": req[11],
            }
            if req
            else None
        )
    except Exception as e:
        # Rollback the transaction if an error occurs
        cnx.rollback()
        raise e


def get_all_requests():
    """
    Retrieves all requests from the database.

    Returns:
        list: A list of dictionaries, each containing request information.
    """
    try:
        # Start a transaction
        cnx.start_transaction()

        # Execute the query to fetch all requests
        cursor.execute(
            f"SELECT id, location, team_id, is_dangerous, creation_date, lead_time, fix_date, status, image, requestor_id, adresse, priority FROM request"
        )
        reqs = cursor.fetchall()

        # Commit the transaction
        cnx.commit()

        return [
            {
                "id": req[0],
                "location": json.loads(req[1]),
                "team_id": req[2],
                "is_dangerous": bool(req[3]),
                "creation_date": req[4],
                "lead_time": req[5],
                "fix_date": req[6],
                "status": req[7],
                "image": req[8],
                "requestor_id": req[9],
                "adresse": req[10],
                "priority": req[11],
            }
            for req in reqs
        ]
    except Exception as e:
        # Rollback the transaction if an error occurs
        cnx.rollback()
        raise e


def insert_request(
    location,
    is_dangerous,
    creation_date,
    adresse,
    status,
    image,
    requestor_id,
    team_id=None,
    lead_time=None,
    fix_date=None,
):
    """
    Inserts a new request into the database.

    Parameters:
        location (str): The location of the request.
        is_dangerous (bool): Indicates if the request is dangerous.
        creation_date (str): The creation date of the request.
        adresse (str): The address associated with the request.
        status (str): The status of the request.
        image (str): The image URL associated with the request.
        requestor_id (int): The ID of the requestor.
        team_id (int, optional): The ID of the team assigned to the request. Defaults to None.
        lead_time (str, optional): The lead time of the request. Defaults to None.
        fix_date (str, optional): The fix date of the request. Defaults to None.

    Returns:
        int or None: The ID of the inserted request if successful, otherwise None.
    """
    try:
        # Start a transaction
        cnx.start_transaction()

        # Execute the query to insert the request
        cursor = cnx.cursor()
        cursor.execute(
            f"INSERT INTO request (location, team_id, is_dangerous, creation_date, adresse, lead_time, fix_date, status, image, requestor_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (
                location,
                team_id,
                is_dangerous,
                creation_date,
                adresse,
                lead_time,
                fix_date,
                status,
                image,
                requestor_id,
            ),
        )

        # Commit the transaction
        cnx.commit()

        # Return the ID of the last inserted row
        return cursor.lastrowid
    except mysql.connector.errors.IntegrityError as e:
        # Rollback the transaction if an integrity error occurs (e.g., duplicate entry)
        cnx.rollback()
        print("Error:", e)
        return None


def modify_request(
    id,
    location=None,
    is_dangerous=None,
    adresse=None,
    status=None,
    image=None,
    team_id=None,
    lead_time=None,
    fix_date=None,
    priority=None,
):
    """
    Modifies an existing request in the database.

    Parameters:
        id (int): The ID of the request to modify.
        location (str, optional): The new location of the request. Defaults to None.
        is_dangerous (bool, optional): Indicates if the request is dangerous. Defaults to None.
        adresse (str, optional): The new address associated with the request. Defaults to None.
        status (str, optional): The new status of the request. Defaults to None.
        image (str, optional): The new image URL associated with the request. Defaults to None.
        team_id (int, optional): The new ID of the team assigned to the request. Defaults to None.
        lead_time (str, optional): The new lead time of the request. Defaults to None.
        fix_date (str, optional): The new fix date of the request. Defaults to None.
        priority (int, optional): The new priority of the request. Defaults to None.

    Returns:
        int: The ID of the modified request.
    """
    try:
        # Start a transaction
        cnx.start_transaction()

        # Construct the SQL UPDATE statement
        query = "UPDATE request SET "
        values = []

        # Append each field to the UPDATE statement if its value is not None
        if location is not None:
            query += "location = %s, "
            values.append(location)
        if is_dangerous is not None:
            query += "is_dangerous = %s, "
            values.append(is_dangerous)
        if adresse is not None:
            query += "adresse = %s, "
            values.append(adresse)
        if status is not None:
            query += "status = %s, "
            values.append(status)
        if image is not None:
            query += "image = %s, "
            values.append(image)
        if team_id is not None:
            query += "team_id = %s, "
            values.append(team_id)
        if lead_time is not None:
            query += "lead_time = %s, "
            values.append(lead_time)
        if fix_date is not None:
            query += "fix_date = %s, "
            values.append(fix_date)
        if priority is not None:
            query += "priority = %s, "
            values.append(priority)

        # Remove the trailing comma and space
        query = query.rstrip(", ")
        query += " WHERE id = %s"
        values.append(id)

        # Execute the UPDATE statement
        cursor = cnx.cursor()
        cursor.execute(query, values)

        # Commit the transaction
        cnx.commit()

        # Close the cursor
        cursor.close()

        return id
    except mysql.connector.errors.IntegrityError as e:
        # Rollback the transaction if an integrity error occurs (e.g., duplicate entry)
        cnx.rollback()
        print("Error:", e)
        return None


def get_all_requestor():
    """
    Retrieves information about all requestors along with their associated requests from the database.

    Returns:
        list: A list containing dictionaries with information about each requestor and their associated requests.
    """
    try:
        # Start a transaction
        cnx.start_transaction()

        # Initialize a cursor
        cursor = cnx.cursor()

        # Retrieve information about all requestors
        cursor.execute(
            "SELECT id, firstname, lastname, adresse, email, tel FROM requestor"
        )
        users = cursor.fetchall()

        # Initialize a list to store requestors and their associated requests
        requestors = []

        # Iterate over each requestor
        for user in users:
            # Extract user information
            user_info = {
                "id": user[0],
                "firstname": user[1],
                "lastname": user[2],
                "adresse": user[3],
                "email": user[4],
                "tel": user[5],
            }

            # Query requests associated with the user
            cursor.execute(
                f"SELECT id, location, adresse, team_id, is_dangerous, creation_date, lead_time, fix_date, status, image, requestor_id, priority FROM request WHERE requestor_id = '{user[0]}'"
            )
            requests = cursor.fetchall()

            # Construct list of request information
            user_requests = []
            for req in requests:
                req_info = {
                    "id": req[0],
                    "location": json.loads(req[1]),
                    "adresse": req[2],
                    "team_id": req[3],
                    "is_dangerous": bool(req[4]),
                    "creation_date": req[5],
                    "lead_time": req[6],
                    "fix_date": req[7],
                    "status": req[8],
                    "image": req[9],
                    "requestor_id": req[10],
                    "priority": req[11],
                }
                user_requests.append(req_info)

            # Append user information along with associated requests to the requestors list
            requestors.append({"info": user_info, "requests": user_requests})

        # Commit the transaction
        cnx.commit()

        return requestors
    except Exception as e:
        # Rollback the transaction if an error occurs
        cnx.rollback()
        print("Error:", e)
        return None


def get_requestor_by_id(id):
    """
    Retrieves information about a requestor with the specified ID from the database.

    Args:
        id (int): The ID of the requestor.

    Returns:
        dict or None: A dictionary containing information about the requestor and their associated requests if found,
                      or None if no requestor with the specified ID is found.
    """
    try:
        # Start a transaction
        cnx.start_transaction()

        # Initialize a cursor
        cursor = cnx.cursor()

        # Retrieve information about the requestor with the specified ID
        cursor.execute(
            f"SELECT id, firstname, lastname, adresse, email, tel FROM requestor WHERE id = '{id}'"
        )
        user = cursor.fetchall()
        user = user[0] if len(user) > 0 else None

        if user:
            # Extract user information
            user_info = {
                "id": user[0],
                "firstname": user[1],
                "lastname": user[2],
                "adresse": user[3],
                "email": user[4],
                "tel": user[5],
            }

            # Retrieve requests associated with the requestor
            cursor.execute(
                f"SELECT id, location, adresse, team_id, is_dangerous, creation_date, lead_time, fix_date, status, image, requestor_id, priority FROM request WHERE requestor_id = '{id}'"
            )
            requests = cursor.fetchall()

            # Construct list of request information
            user_requests = []
            for req in requests:
                req_info = {
                    "id": req[0],
                    "location": json.loads(req[1]),
                    "adresse": req[2],
                    "team_id": req[3],
                    "is_dangerous": bool(req[4]),
                    "creation_date": req[5],
                    "lead_time": req[6],
                    "fix_date": req[7],
                    "status": req[8],
                    "image": req[9],
                    "requestor_id": req[10],
                    "priority": req[10],
                }
                user_requests.append(req_info)

            # Commit the transaction
            cnx.commit()

            return {"info": user_info, "requests": user_requests}
        else:
            # Commit the transaction
            cnx.commit()

            return None
    except Exception as e:
        # Rollback the transaction if an error occurs
        cnx.rollback()
        print("Error:", e)
        return None


def get_requestor_by_tel(tel):
    """
    Retrieves information about a requestor with the specified telephone number from the database.

    Args:
        tel (str): The telephone number of the requestor.

    Returns:
        dict or None: A dictionary containing information about the requestor if found,
                      or None if no requestor with the specified telephone number is found.
    """
    try:
        # Start a transaction
        cnx.start_transaction()

        # Initialize a cursor
        cursor = cnx.cursor()

        # Retrieve information about the requestor with the specified telephone number
        cursor.execute(
            f"SELECT id, firstname, lastname, adresse, email, tel FROM requestor WHERE tel = '{tel}'"
        )
        user = cursor.fetchall()
        user = user[0] if len(user) > 0 else None

        # Close the cursor
        cursor.close()

        # Commit the transaction
        cnx.commit()

        return (
            {
                "id": user[0],
                "firstname": user[1],
                "lastname": user[2],
                "adresse": user[3],
                "email": user[4],
                "tel": user[5],
            }
            if user
            else None
        )
    except Exception as e:
        # Rollback the transaction if an error occurs
        cnx.rollback()
        print("Error:", e)
        return None


def get_requestor_by_name_and_address(firstname, lastname, adresse):
    """
    Retrieves information about a requestor with the specified first name, last name, and address from the database.

    Args:
        firstname (str): The first name of the requestor.
        lastname (str): The last name of the requestor.
        adresse (str): The address of the requestor.

    Returns:
        dict or None: A dictionary containing information about the requestor if found,
                      or None if no requestor with the specified details is found.
    """
    try:
        # Start a transaction
        cnx.start_transaction()

        # Initialize a cursor
        cursor = cnx.cursor()

        # Retrieve information about the requestor with the specified details
        cursor.execute(
            f"SELECT id, firstname, lastname, adresse, email, tel FROM requestor WHERE firstname = '{firstname}' AND lastname = '{lastname}' AND adresse = '{adresse}'"
        )
        user = cursor.fetchall()
        user = user[0] if len(user) > 0 else None

        # Close the cursor
        cursor.close()

        # Commit the transaction
        cnx.commit()

        return (
            {
                "id": user[0],
                "firstname": user[1],
                "lastname": user[2],
                "adresse": user[3],
                "email": user[4],
                "tel": user[5],
            }
            if user
            else None
        )
    except Exception as e:
        # Rollback the transaction if an error occurs
        cnx.rollback()
        print("Error:", e)
        return None


def get_requestor_by_name_and_tel(firstname, lastname, tel):
    """
    Retrieves information about a requestor with the specified first name, last name, and telephone number from the database.

    Args:
        firstname (str): The first name of the requestor.
        lastname (str): The last name of the requestor.
        tel (str): The telephone number of the requestor.

    Returns:
        dict or None: A dictionary containing information about the requestor if found,
                      or None if no requestor with the specified details is found.
    """
    try:
        # Start a transaction
        cnx.start_transaction()

        # Initialize a cursor
        cursor = cnx.cursor()

        # Retrieve information about the requestor with the specified details
        cursor.execute(
            f"SELECT id, firstname, lastname, adresse, email, tel FROM requestor WHERE firstname = '{firstname}' AND lastname = '{lastname}' AND tel = '{tel}'"
        )
        user = cursor.fetchall()
        user = user[0] if len(user) > 0 else None

        # Close the cursor
        cursor.close()

        # Commit the transaction
        cnx.commit()

        return (
            {
                "id": user[0],
                "firstname": user[1],
                "lastname": user[2],
                "adresse": user[3],
                "email": user[4],
                "tel": user[5],
            }
            if user
            else None
        )
    except Exception as e:
        # Rollback the transaction if an error occurs
        cnx.rollback()
        print("Error:", e)
        return None


def get_requestor_by_email(email):
    """
    Retrieves information about a requestor with the specified email address from the database.

    Args:
        email (str): The email address of the requestor.

    Returns:
        dict or None: A dictionary containing information about the requestor if found,
                      or None if no requestor with the specified email address is found.
    """
    try:
        # Start a transaction
        cnx.start_transaction()

        # Initialize a cursor
        cursor = cnx.cursor()

        # Retrieve information about the requestor with the specified email address
        cursor.execute(
            f"SELECT id, firstname, lastname, adresse, email, tel FROM requestor WHERE email = '{email}'"
        )
        user = cursor.fetchall()
        user = user[0] if len(user) > 0 else None

        # Close the cursor
        cursor.close()

        # Commit the transaction
        cnx.commit()

        return (
            {
                "id": user[0],
                "firstname": user[1],
                "lastname": user[2],
                "adresse": user[3],
                "email": user[4],
                "tel": user[5],
            }
            if user
            else None
        )
    except Exception as e:
        # Rollback the transaction if an error occurs
        cnx.rollback()
        print("Error:", e)
        return None


def insert_requestor(
    firstname,
    lastname,
    email,
    tel,
    adresse=None,
):
    """
    Inserts a new requestor into the database with the provided information.

    Args:
        firstname (str): The first name of the requestor.
        lastname (str): The last name of the requestor.
        email (str): The email address of the requestor.
        tel (str): The telephone number of the requestor.
        adresse (str, optional): The address of the requestor. Defaults to None.

    Returns:
        int: The ID of the newly inserted requestor.
    """
    try:
        # Start a transaction
        cnx.start_transaction()

        # Initialize a cursor
        cursor = cnx.cursor()

        # Insert the new requestor into the database
        cursor.execute(
            "INSERT INTO requestor (firstname, lastname, adresse, email, tel) VALUES (%s, %s, %s, %s, %s)",
            (firstname, lastname, adresse, email, tel),
        )

        # Get the ID of the last inserted row
        last_insert_id = cursor.lastrowid

        # Commit the transaction
        cnx.commit()

        # Close the cursor
        cursor.close()

        return last_insert_id
    except Exception as e:
        # Rollback the transaction if an error occurs
        cnx.rollback()
        print("Error:", e)
        return None


def modify_requestor(
    id, firstname=None, lastname=None, email=None, tel=None, adresse=None
):
    """
    Modifies the information of an existing requestor in the database.

    Args:
        id (int): The ID of the requestor to modify.
        firstname (str, optional): The new first name of the requestor. Defaults to None.
        lastname (str, optional): The new last name of the requestor. Defaults to None.
        email (str, optional): The new email address of the requestor. Defaults to None.
        tel (str, optional): The new telephone number of the requestor. Defaults to None.
        adresse (str, optional): The new address of the requestor. Defaults to None.

    Returns:
        int: The ID of the modified requestor.
    """
    try:
        # Start a transaction
        cnx.start_transaction()

        # Initialize a cursor
        cursor = cnx.cursor()

        # Construct the SQL UPDATE statement
        query = "UPDATE requestor SET "
        values = []

        # Append each field to the UPDATE statement if its value is not None
        if firstname is not None:
            query += "firstname = %s, "
            values.append(firstname)
        if lastname is not None:
            query += "lastname = %s, "
            values.append(lastname)
        if email is not None:
            query += "email = %s, "
            values.append(email)
        if tel is not None:
            query += "tel = %s, "
            values.append(tel)
        if adresse is not None:
            query += "adresse = %s, "
            values.append(adresse)

        # Remove the trailing comma and space
        query = query.rstrip(", ")
        query += " WHERE id = %s"
        values.append(id)

        # Execute the SQL UPDATE statement
        cursor.execute(query, values)

        # Commit the transaction
        cnx.commit()

        # Close the cursor
        cursor.close()

        return id
    except Exception as e:
        # Rollback the transaction if an error occurs
        cnx.rollback()
        print("Error:", e)
        return None
