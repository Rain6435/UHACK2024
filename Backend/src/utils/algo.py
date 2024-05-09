# Importing necessary modules and classes
from geopy.distance import geodesic
from geopy.geocoders import GoogleV3
from datetime import datetime

# Importing custom module
from utils.dijkistra import dijkistra_magic

# Dictionary mapping street types to their priority levels
street_priority = {
    "Autoroute": 1,
    "Boulevard": 1,
    "Promenade": 1,
    "Avenue": 2,
    "Route": 2,
    "Rue": 2,
    "Chemin": 2,
    "Corridor": 2,
    "Montée": 3,
    "Place": 3,
    "Ruelle": 3,
    "Impasse": 3,
    "Allée": 3,
    "Croissant": 3,
}


def schedule_potholes(potholes, teams):
    """
    Schedules pothole repairs by organizing and assigning them to teams.

    Parameters:
        potholes (list): List of potholes to be repaired.
        teams (list): List of teams available for pothole repair.

    Returns:
        dict: A dictionary where each team is assigned a list of potholes to repair.
    """

    # Organize potholes based on their priority and danger level
    sorted_potholes = organize_potholes(potholes)

    # Get the optimal sequence of potholes to repair using Dijkstra's algorithm
    chain_of_potholes = dijkistra_magic(sorted_potholes, calculate_distance)

    # Assign potholes to teams while respecting the maximum work time constraint
    max_work_time = 480  # Maximum threshold of time worked in minutes
    team_assignments = assign_potholes(chain_of_potholes, len(teams), max_work_time)

    # Format the output to map potholes to their respective teams
    return format_output(team_assignments, teams)


def organize_potholes(potholes):
    """
    Organizes potholes into different categories based on priority and danger level.

    Parameters:
        potholes (list): List of potholes to be organized.

    Returns:
        dict: A dictionary containing sorted potholes categorized by priority and danger level.
    """

    sorted_potholes = {
        "dangerous": {
            "main": [],
            "collector": [],
            "local": [],
        },
        "non-dangerous": {
            "main": [],
            "collector": [],
            "local": [],
        },
    }

    for pothole in potholes:
        # Get the street type to classify the pothole
        street = pothole["segment"]

        # Categorize potholes based on danger level and street priority
        if pothole["is_dangerous"]:
            if street_priority[street] == 1:
                sorted_potholes["dangerous"]["main"].append(pothole)
            elif street_priority[street] == 2:
                sorted_potholes["dangerous"]["collector"].append(pothole)
            elif street_priority[street] == 3:
                sorted_potholes["dangerous"]["local"].append(pothole)
            else:
                # Should never reach here, log error if encountered
                pass
        else:
            if street_priority[street] == 1:
                sorted_potholes["non-dangerous"]["main"].append(pothole)
            elif street_priority[street] == 2:
                sorted_potholes["non-dangerous"]["collector"].append(pothole)
            elif street_priority[street] == 3:
                sorted_potholes["non-dangerous"]["local"].append(pothole)
            else:
                # Should never reach here, log error if encountered
                pass

    # Sort potholes in their respective lists by age
    for category in sorted_potholes.values():
        for sub_category in category.values():
            sub_category.sort(key=lambda x: date_to_number(x))

    return sorted_potholes


def assign_potholes(chain_of_potholes, nb_of_teams, max_work_time):
    """
    Assigns potholes to teams while respecting maximum work time constraints.

    Parameters:
        chain_of_potholes (list): List of potholes sorted by priority for repair.
        nb_of_teams (int): Number of available teams for pothole repair.
        max_work_time (int): Maximum threshold of time worked in minutes.

    Returns:
        list: List of lists where each inner list represents the potholes assigned to a team.
    """

    # Constants for average moving speed and pothole repair time
    speed = 45  # Average moving speed in km/h
    repair_time = 25  # Pothole repair time in minutes

    # Initialize each team with no assigned work
    teams_workload = [[0, []] for _ in range(nb_of_teams)]

    # Iterate through each team and assign potholes based on maximum work time
    pothole_nb = 0  # Current pothole index in chain
    for team_nb in range(nb_of_teams):
        while True and pothole_nb < len(chain_of_potholes):
            # If no potholes currently assigned, directly assign one
            if not teams_workload[team_nb][1]:
                teams_workload[team_nb] = [15, [chain_of_potholes[pothole_nb]]]
                pothole_nb += 1
            else:
                # Calculate the travel distance between current and last assigned pothole
                travel_distance = calculate_distance(
                    chain_of_potholes[pothole_nb], teams_workload[team_nb][1][-1]
                )

                # Calculate new work time after adding the next pothole
                new_time = (
                    teams_workload[team_nb][0] + repair_time + travel_distance / speed
                )

                # Check if the team can accept the next pothole within the maximum work time
                if new_time < max_work_time:
                    teams_workload[team_nb][0] = new_time
                    teams_workload[team_nb][1].append(chain_of_potholes[pothole_nb])
                    pothole_nb += 1
                else:
                    # Move to the next team if the current team cannot accept the pothole
                    break

    # Return only the list of potholes assigned to each team
    return [team[1] for team in teams_workload]


def format_output(team_assignments, team_ids):
    """
    Formats the output to map potholes to their respective teams.

    Parameters:
        team_assignments (list): List of lists where each inner list represents the potholes assigned to a team.
        team_ids (list): List of team IDs.

    Returns:
        dict: A dictionary where each team ID is mapped to a dictionary of assigned potholes with priority indices.
    """

    output = {}

    for i, team_id in enumerate(team_ids):
        curr_pothole_dict = {}
        for ind, pothole in enumerate(team_assignments[i]):
            curr_pothole_dict[ind] = pothole

        output[team_id] = curr_pothole_dict

    return output


def date_to_number(pothole, format="%Y-%m-%d", reference_date=datetime.now()):
    """
    Converts a date string to a numerical value representing the age of the pothole.

    Parameters:
        pothole (dict): Pothole object containing the date information.
        format (str): Date format string (default is '%Y-%m-%d').
        reference_date (datetime): Reference date for calculating age (default is current date).

    Returns:
        int: Numerical value representing the age of the pothole in days.
    """
    date_object = datetime.strptime(pothole["date"], format)
    delta = reference_date - date_object
    return delta.days


def calculate_distance(pothole1, pothole2, use_age=False):
    """
    Calculates the distance between two potholes.

    Parameters:
        pothole1 (dict): First pothole object containing address information.
        pothole2 (dict): Second pothole object containing address information.
        use_age (bool): Flag indicating whether to use age for distance calculation (default is False).

    Returns:
        float: Distance between the two potholes in kilometers.
    """
    address1 = pothole1["address"]
    address2 = pothole2["address"]

    geolocator = GoogleV3(api_key="", user_agent="Potholes", timeout=30)
    location1 = geolocator.geocode(address1)
    location2 = geolocator.geocode(address2)

    coords1 = (location1.latitude, location1.longitude)
    coords2 = (location2.latitude, location2.longitude)

    # Adjust distance calculation based on pothole age if required
    if use_age:
        return geodesic(coords1, coords2).kilometers - date_to_number
    else:
        return geodesic(coords1, coords2).kilometers
