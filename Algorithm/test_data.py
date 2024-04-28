from faker import Faker
from datetime import datetime, timedelta
import random
from algo import schedule_potholes

fake = Faker()

ottawa_addresses = [
    "24 Sussex Drive, Ottawa, Canada",
    "111 Sussex Drive, Ottawa, Canada",
    "112 Sussex Drive, Ottawa, Canada",
    "113 Sussex Drive, Ottawa, Canada",
    "114 Sussex Drive, Ottawa, Canada",
    "115 Sussex Drive, Ottawa, Canada",
    "116 Sussex Drive, Ottawa, Canada",
    "2 Colonel By Drive, Ottawa, Canada",
    "123 Slater Street, Ottawa, Canada",
    "124 Slater Street, Ottawa, Canada",
    "125 Slater Street, Ottawa, Canada",
    "126 Slater Street, Ottawa, Canada",
    "127 Slater Street, Ottawa, Canada",
    "150 Elgin Street, Ottawa, Canada",
    "100 Laurier Avenue W, Ottawa, Canada",
    "55 Colonel By Drive, Ottawa, Canada",
    "1 Vimy Place, Ottawa, Canada",
    "10 Blackburn Avenue, Ottawa, Canada",
    "1 Rideau Street, Ottawa, Canada",
    "900 Montreal Road, Ottawa, Canada",
    "100 Bayshore Drive, Ottawa, Canada",
    "240 Sparks Street, Ottawa, Canada",
    "401 Smyth Road, Ottawa, Canada",
    "1385 Woodroffe Avenue, Ottawa, Canada",
    "295 Montreal Road, Ottawa, Canada",
    "290 Dupuis Street, Ottawa, Canada",
    "1755 Russell Road, Ottawa, Canada",
    "333 River Road, Ottawa, Canada",
    "1200 St Laurent Boulevard, Ottawa, Canada",
    "101 Centrepointe Drive, Ottawa, Canada",
    "1600 Stittsville Main Street, Ottawa, Canada",
    "100 Constellation Drive, Ottawa, Canada",
    "141 Catherine Street, Ottawa, Canada",
    "1000 Palladium Drive, Ottawa, Canada",
    "100 Malvern Drive, Ottawa, Canada",
    "100 Charlie Rogers Place, Ottawa, Canada",
    "4801 Riverside Drive, Ottawa, Canada",
    "1000 Innovation Drive, Ottawa, Canada",
    "4899 Uplands Drive, Ottawa, Canada",
    "200 Elgin Street, Ottawa, Canada",
    "240 Bank Street, Ottawa, Canada",
    "111 Albert Street, Ottawa, Canada",
    "160 George Street, Ottawa, Canada",
    "55 Murray Street, Ottawa, Canada",
    "130 Sparks Street, Ottawa, Canada",
    "1500 Carling Avenue, Ottawa, Canada",
    "2900 Woodroffe Avenue, Ottawa, Canada",
    "955 Green Valley Crescent, Ottawa, Canada",
    "359 Terry Fox Drive, Ottawa, Canada"
]

def get_random_address(index):
    return ottawa_addresses[index]

potholes = []
for i in range(10):
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

results = schedule_potholes(potholes, [0 for _ in range(3)])

# Print the test data
for i in range(len(results)):
    team = results[i]
    print("team " + str(i))
    for pothole in team:
        print(pothole)
    print("\n")
