from datetime import date

MSG = "Hey {}, there are more people with your birthday!"


class BirthdayDict(dict):
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    def __init__(self, *args, **kwargs):
        self.update(*args, **kwargs)

    def _get_month_day(self, birthday):
        return (birthday.month, birthday.day)

    def __setitem__(self, name, birthday):
        my_month_day = self._get_month_day(birthday)
        for other_bd in self.values():
            if self._get_month_day(other_bd) == my_month_day:
                print(MSG.format(name))
        dict.__setitem__(self, name, birthday)
