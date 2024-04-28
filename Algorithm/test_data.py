from faker import Faker
from datetime import datetime, timedelta
import random
from algo import schedule_potholes

fake = Faker()

gatineau_addresses = [
    "230 Bd Saint-Joseph, Gatineau, QC J8Y 3X4, Canada",
    "92 Rue Labelle, Gatineau, QC J8Y, Canada",
    "Prom. de la Gatineau, Chelsea, QC, Canada",
    "77 Rue Sherbrooke, Gatineau, QC J8Y 2K8, Canada",
    "788 Bd la Vérendrye O, Gatineau, QC J8R 4A8, Canada",
    "230 Rue Saint-Louis, Gatineau, QC J8P 8B3, Canada",
    "11 Rue de la Comète, Gatineau, QC J9A 2Y3, Canada",
    "25 Baie St, Gatineau, Canada",
    "80 Bellehumeur St, Gatineau, Canada",
    "200 Montcalm St, Gatineau, Canada",
    "100 Gappe Blvd, Gatineau, Canada",
    "350 Cité-des-Jeunes Blvd, Gatineau, Canada",
    "150 Hôtel-de-Ville St, Gatineau, Canada",
    "50 Bellehumeur St, Gatineau, Canada",
    "75 Edmonton St, Gatineau, Canada",
    "275 Cité-des-Jeunes Blvd, Gatineau, Canada",
    "250 Cité-des-Jeunes Blvd, Gatineau, Canada",
    "1 Plateau Blvd, Gatineau, Canada",
    "75 Gappe Blvd, Gatineau, Canada",
    "100 Hôpital Blvd, Gatineau, Canada",
    "200 Gréber Blvd, Gatineau, Canada",
    "125 Cité-des-Jeunes Blvd, Gatineau, Canada",
    "50 Charlevoix St, Gatineau, Canada",
    "200 Allumettières Blvd, Gatineau, Canada",
    "150 Hôpital Blvd, Gatineau, Canada",
    "300 Saint-Joseph Blvd, Gatineau, Canada",
    "100 Georges-Bilodeau St, Gatineau, Canada",
    "75 Georges-Bilodeau St, Gatineau, Canada",
    "50 Georges-Bilodeau St, Gatineau, Canada",
    "125 Georges-Bilodeau St, Gatineau, Canada",
    "150 Georges-Bilodeau St, Gatineau, Canada",
    "175 Georges-Bilodeau St, Gatineau, Canada",
    "200 Georges-Bilodeau St, Gatineau, Canada",
    "225 Georges-Bilodeau St, Gatineau, Canada",
    "250 Georges-Bilodeau St, Gatineau, Canada",
    "275 Georges-Bilodeau St, Gatineau, Canada",
    "300 Georges-Bilodeau St, Gatineau, Canada",
    "325 Georges-Bilodeau St, Gatineau, Canada",
    "350 Georges-Bilodeau St, Gatineau, Canada"
]

def get_random_address(index):
    return gatineau_addresses[index]

potholes = []
for i in range(7):
    address = get_random_address(i)
    dangerous = random.choice([True, False])
    date = fake.date_time_between(start_date='-1y', end_date='now').strftime('%Y-%m-%d')
    segment = random.choice(["Autoroute", "Boulevard", "Promenade", "Avenue", "Route", "Rue", "Chemin", "Corridor", "Montée", "Place", "Ruelle", "Impasse", "Allée", "Croissant"])
    potholes.append({
        'address': address,
        'is_dangerous': dangerous,
        'date': date,
        'segment': segment
    })

results = schedule_potholes(potholes, [3*i for i in range(3)])


for team in results.keys():
    print(str(team))
    for pothole in results[team].items():
        print(pothole)
    print("\n")
