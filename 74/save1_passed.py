import calendar
from datetime import date

def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    return calendar.day_name[date.weekday()]
    
print(weekday_of_birth_date(date(1968, 9, 25)))