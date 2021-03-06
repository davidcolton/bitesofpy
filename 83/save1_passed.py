from pytz import timezone, utc
from datetime import datetime


AUSTRALIA = timezone('Australia/Sydney')
SPAIN = timezone('Europe/Madrid')


def what_time_lives_pybites(naive_utc_dt):
    """Receives a naive UTC datetime object and returns a two element
       tuple of Australian and Spanish (timezone aware) datetimes"""
    utc_dt = datetime(naive_utc_dt.year,
                      naive_utc_dt.month,
                      naive_utc_dt.day,
                      naive_utc_dt.hour,
                      naive_utc_dt.minute,
                      0, 
                      tzinfo=utc)
                      
    return(utc_dt.astimezone(AUSTRALIA),
           utc_dt.astimezone(SPAIN))
