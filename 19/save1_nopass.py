from datetime import datetime

NOW = datetime.now()

class Promo:
    def __init__(self, name, expires):
        self.name = name
        self.expires = expires
        
    def get_expired(self):
        print('Getting expired value')
        return self._expired
        
    def set_expired(self):
        if NOW <= self.expires:
            self._expired = False
        else:
            self._expired = True
            
    expired = property(get_expired, set_expired)