from datetime import datetime
from datetime import timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)

def gen_special_pybites_dates():
    pybites_date = PYBITES_BORN
    while pybites_date < datetime.now():
        pybites_date = pybites_date + timedelta(days=100)
        yield pybites_date