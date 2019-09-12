from collections import defaultdict
from pathlib import Path
from urllib.request import urlretrieve

from bs4 import BeautifulSoup as bs

# import the countries xml file
tmp = Path("/tmp")
countries = tmp / "countries.xml"

if not countries.exists():
    urlretrieve("https://bit.ly/2IzGKav", countries)


def get_income_distribution(xml=countries):
    """
    - Read in the countries xml as stored in countries variable.
    - Parse the XML
    - Return a dict of:
      - keys = incomes (wb:incomeLevel)
      - values = list of country names (wb:name)
    """
    income_dist = defaultdict(list)
    with open(xml, "r") as f:
        contents = f.read()
        soup = bs(contents, "html")
        countries = soup.find_all(r"wb:country")
        for country in countries:
            income_level = country.find(r"wb:incomelevel").text
            name = country.find(r"wb:name").text
            income_dist[income_level].append(name)
    return income_dist


get_income_distribution()
