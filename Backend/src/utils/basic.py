import re  # Importing the re module for regular expression operations


def format_tel(tel: str):
    """
    Formats a telephone number by removing all non-numeric characters.

    Parameters:
        tel (str): The telephone number to format.

    Returns:
        str or None: The formatted telephone number, or None if the input is empty.
    """
    if not tel:  # If input is empty
        return None

    digits = re.findall(r"\d", tel)  # Find all numeric digits in the input

    return "".join(digits)  # Join the numeric digits into a single string


def format_name(name: str):
    """
    Formats a name by converting it to lowercase.

    Parameters:
        name (str): The name to format.

    Returns:
        str or None: The formatted name in lowercase, or None if the input is empty.
    """
    if not name:  # If input is empty
        return None

    return name.lower()  # Convert the name to lowercase
