from flask import Response, abort

# Custom imports
from utils.api_wrapper import (
    return_error_response,
    HTTP_CODE_UNAUTHORIZED,
    MIME_TYPE_JSON,
)
from utils.db import (
    get_requestor_by_id,
    get_all_requestor,
    get_requestor_by_name_and_tel,
    insert_requestor,
    modify_requestor,
)
from utils.basic import format_tel, format_name


def get_requestors(request):
    """
    Retrieve requestors based on provided query parameters.

    Args:
        request: Flask request object.

    Returns:
        If ID is provided, returns the requestor with that ID,
        otherwise returns all requestors.
    """
    id = request.args.get("id", None)

    if id:
        return get_requestor_by_id(id)
    else:
        return get_all_requestor()


def login_requestor(request):
    """
    Log in a requestor based on provided first name, last name, and telephone number.

    Args:
        request: Flask request object.

    Returns:
        Requestor information if successfully logged in,
        otherwise returns an error response.
    """
    body = request.json

    firstname = format_name(body.get("firstname"))
    lastname = format_name(body.get("lastname"))
    tel = format_tel(body.get("tel"))

    if tel and firstname and lastname:
        user = get_requestor_by_name_and_tel(
            firstname=firstname, lastname=lastname, tel=tel
        )
    else:
        abort(
            Response(
                return_error_response("ERR_GENERAL_E001", "INVALID"),
                HTTP_CODE_UNAUTHORIZED,
                content_type=MIME_TYPE_JSON,
            )
        )
    if not user:
        abort(
            Response(
                return_error_response("ERR_GENERAL_E001", "INVALID"),
                HTTP_CODE_UNAUTHORIZED,
                content_type=MIME_TYPE_JSON,
            )
        )

    return user


def create_requestor(request):
    """
    Create or modify a requestor based on provided data.

    Args:
        request: Flask request object.

    Returns:
        ID of the created or modified requestor,
        or an error response if the operation fails.
    """
    body = request.json
    firstname = format_name(body.get("firstname"))
    lastname = format_name(body.get("lastname"))
    tel = format_tel(body.get("tel"))
    email = body.get("email")
    adresse = body.get("adresse")
    id = body.get("id")

    if request.method == "POST":
        requestor_id = insert_requestor(
            firstname=firstname,
            lastname=lastname,
            tel=tel,
            email=email,
            adresse=adresse,
        )
    elif id:
        requestor_id = modify_requestor(
            id=id,
            firstname=firstname,
            lastname=lastname,
            tel=tel,
            email=email,
            adresse=adresse,
        )
    else:
        abort(
            Response(
                return_error_response("ERR_GENERAL_E001", "INVALID id"),
                HTTP_CODE_UNAUTHORIZED,
                content_type=MIME_TYPE_JSON,
            )
        )

    return requestor_id


def delete_requestor(request):
    """
    Placeholder function for deleting a requestor.

    Args:
        request: Flask request object.

    Returns:
        An empty string.
    """
    return ""
