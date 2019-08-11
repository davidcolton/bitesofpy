from datetime import datetime
from datetime import timedelta

NOW = datetime.now()

class Promo:
    def __init__(self, name, expires):
        self.name = name
        self.expires = expires

    @property       
    def expired(self):
        if NOW <= self.expires:
            return False
        else:
            return True