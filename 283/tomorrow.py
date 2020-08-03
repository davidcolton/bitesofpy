import datetime


def tomorrow(today = None):
    if today is None:
        return (datetime.datetime.now() + datetime.timedelta(days=1)).date()
    else:
        return  today + datetime.timedelta(days=1)
