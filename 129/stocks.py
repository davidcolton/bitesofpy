import requests
from collections import defaultdict
from collections import Counter

STOCK_DATA = "https://bit.ly/2MzKAQg"

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float"""
    if cap == "n/a":
        return 0
    elif cap[-1] == "M":
        return float(cap[1:-1])
    elif cap[-1] == "B":
        return float(cap[1:-1]) * 1000


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    inductry_cap = Counter()
    for ticket in data:
        inductry_cap[ticket["industry"].strip()] += _cap_str_to_mln_float(ticket["cap"])
    return round(inductry_cap[industry], 2)


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    market_cap = dict()
    for ticket in data:
        market_cap[ticket["symbol"]] = _cap_str_to_mln_float(ticket["cap"])
    return max(market_cap, key=market_cap.get)


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    max_min_stocks = Counter()
    for ticket in data:
        if ticket["sector"] != "n/a":
            max_min_stocks[ticket["sector"]] += 1

    return (max_min_stocks.most_common(1)[0][0], max_min_stocks.most_common()[-1][0])

