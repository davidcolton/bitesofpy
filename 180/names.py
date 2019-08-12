import csv
from collections import defaultdict

# fake data from https://www.mockaroo.com
data = """last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN"""


def group_names_by_country(data: str = data) -> defaultdict:
    # Empty, new DefaultDictionary
    countries = defaultdict(list)

    # Use DictReader so we can reference the values by name
    users = csv.DictReader(data.split('\n'))

    #Add each user in the required format and return
    for user in users:
        cc = user['country_code']
        fn = user['first_name']
        ln = user['last_name']
        countries[cc].append(f'{fn} {ln}')
    return countries
