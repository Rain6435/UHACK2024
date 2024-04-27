from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from dijkistra import dijkistra_magic
from datetime import datetime


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

def schedule_potholes(potholes, teams, streets):
    '''
    Inputs:
        list of potholes
        list of teams: used to 
        list of streets: used to determine priority by
                            main arteries > collector streets > local street

    Returns:
        list of teams, for which each team has a list of potholes
    '''

    # Separate the dangerous potholes before the non-dangerous, then by street priority,
    #  then by age

    sorted_potholes = organize_potholes(potholes)

    # Get dijkistra for subgraphs dangerous and non-dangerous, and for each, subgraphs
    #  for Main, Connecting, and Local arteries
    #  Those are joined together into 1 chain of potholes before being returned

    chain_of_potholes = dijkistra_magic(sorted_potholes, calculate_distance)

    # Now we will separate this chain of potholes in an equitable way, that takes
    # max threshold of hours worked

    max_work_time = 480 # in minutes

    team_assignments = assign_potholes(chain_of_potholes, len(teams), max_work_time)

    return team_assignments


def organize_potholes(potholes):
    '''
    Returns a list of potholes sorted in the following way:
        {
            "dangerous": {
                "main": [ <sorted by age> ] ,
                "collector": [ <sorted by age> ] ,
                "local": [ <sorted by age> ]
            } ,
            "non-dangerous": {
                "main": [ <sorted by age> ] ,
                "collector": [ <sorted by age> ] ,
                "local": [ <sorted by age> ]
            }
        }
    '''

    sorted_potholes = {
        "dangerous": {
            "main": [] ,
            "collector": [] ,
            "local": [] ,
        }, 
        "non-dangerous": {
            "main": [] ,
            "collector": [] ,
            "local": [] ,
        }
    }

    for pothole in potholes:
        if pothole.is_dangerous:
            # Get the string attribute GENERIQUE, to classify the potholes
            street = pothole.location.segment # TODO: update this to correctly get street
            if street_priority[street] == 1:
                sorted_potholes["dangerous"]["main"].append(pothole)
            if street_priority[street] == 2:
                sorted_potholes["dangerous"]["collector"].append(pothole)
            if street_priority[street] == 3:
                sorted_potholes["dangerous"]["local"].append(pothole)
            else:
                # should never be here, show error if that's the case
                pass
        else:
            # Get the string attribute GENERIQUE, to classify the potholes
            street = pothole.location.segment # TODO: update this to correctly get street
            if street_priority[street] == 1:
                sorted_potholes["non-dangerous"]["main"].append(pothole)
            if street_priority[street] == 2:
                sorted_potholes["non-dangerous"]["collector"].append(pothole)
            if street_priority[street] == 3:
                sorted_potholes["non-dangerous"]["local"].append(pothole)
            else:
                # should never be here, show error if that's the case
                pass
    
    # Sort potholes in their respective lists
    sorted(sorted_potholes["dangerous"]["main"], key=date_to_number)
    sorted(sorted_potholes["dangerous"]["collector"], key=date_to_number)
    sorted(sorted_potholes["dangerous"]["local"], key=date_to_number)
    sorted(sorted_potholes["non-dangerous"]["main"], key=date_to_number)
    sorted(sorted_potholes["non-dangerous"]["collector"], key=date_to_number)
    sorted(sorted_potholes["non-dangerous"]["local"], key=date_to_number)

    return sorted_potholes


def calculate_distance(pothole1, pothole2):
    '''
    Get distance between two potholes
    '''
    # TODO: make sure we are getting address correctly
    address1 = pothole1.address
    address2 = pothole2.address

    geolocator = Nominatim(user_agent="Potholes")

    location1 = geolocator.geocode(address1)
    location2 = geolocator.geocode(address2)

    coords1 = (location1.latitude, location1.longitude)
    coords2 = (location2.latitude, location2.longitude)

    return geodesic(coords1, coords2).kilometers


def date_to_number(pothole, format='%Y-%m-%d', reference_date=datetime(1970, 1, 1)):
    '''
    Return a numerical value given an SQL data object 
    '''
    date_object = datetime.strptime(pothole.date, format)
    delta = date_object - reference_date
    return delta.days


def get_address_string(pothole):
    '''
    Get address string from pothole object
    '''
    return pothole.location.string_location # TODO: make this work


def assign_potholes(chain_of_potholes, nb_of_teams, max_work_time):
    '''
    Separate the potholes into each time while repescting a normal work day
    Inputs:
         chain_of_potholes: list of potholes
         nb_of_teams: number of teams
         max_work_time: maximum threshold of time worked (minutes)
    '''
    # Assuming an average moving speed of 45km/h, and a pothole repair to last 15 minutes
    speed = 45
    repair_time = 15

    # initialize each team as having no work
    teams_workload = [(0, []) for x in range(nb_of_teams)]

    # Current pothole index in chain
    pothole_nb = 0

    # We will try to assign potholes by fully booking one team and moving to the next one
    for team_nb in range(nb_of_teams):
        # Fully book this team as much as possible

        while True and pothole_nb < len(chain_of_potholes):
            # If no potholes currently assigned, directly assign one
            if teams_workload[team_nb][1] == []:
                teams_workload[team_nb] = (15, [chain_of_potholes[pothole_nb]])

                pothole_nb += 1
            else:
                # Get distance between current pothole to assign and last given
                # pothole to the team
                travel_distance = calculate_distance(chain_of_potholes[pothole_nb], teams_workload[team_nb][1][-1])

                # Calculate the new work time after adding the next pothole to repair to current team
                new_time = teams_workload[team_nb][0] + repair_time + travel_distance / speed

                # Check if the current team can get assigned this pothole
                if new_time < max_work_time:
                    teams_workload[team_nb][0] = new_time
                    teams_workload[team_nb][1].append(chain_of_potholes[pothole_nb])

                    pothole_nb += 1
                else:
                    # This team can't accept this pothole, so we move to the next team in the list
                    break

    
    # Return only the list of potholes the teams will work on
    return [team[1] for team in teams_workload]

        



