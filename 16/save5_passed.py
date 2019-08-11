from datetime import datetime
from datetime import timedelta
from datetime import date


PYBITES_BORN = datetime(year=2016, month=12, day=19)

def gen_special_pybites_dates():
    pybites_days = PYBITES_BORN
    pybites_years = PYBITES_BORN
    while pybites_days < datetime.now():
        if pybites_days + timedelta(days=100) < pybites_years + timedelta(days=365):
            pybites_days = pybites_days + timedelta(days=100)
            yield pybites_days
        else:
            pybites_years = pybites_years + timedelta(days=365)
            yield pybites_years
