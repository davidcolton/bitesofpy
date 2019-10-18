from random import random
from time import sleep
from functools import wraps


def cached_property(func):
    """decorator used to cache expensive object attribute lookup"""
    planet_mass_dict = dict()

    @wraps(func)
    def wrapper(*args):
        if args in planet_mass_dict:
            return planet_mass_dict[args]
        else:
            planet_mass = func(*args)
            planet_mass_dict[args] = planet_mass
            return planet_mass

    return wrapper


class Planet:
    """the nicest little orb this side of Orion's Belt"""

    GRAVITY_CONSTANT = 42
    TEMPORAL_SHIFT = 0.12345
    SOLAR_MASS_UNITS = "M\N{SUN}"

    def __init__(self, color):
        self.color = color
        self._mass = None

    def __repr__(self):
        return f"{self.__class__.__name__}({repr(self.color)})"

    @property
    @cached_property
    def mass(self):
        scale_factor = random()
        sleep(self.TEMPORAL_SHIFT)
        planet_mass = (
            f"{round(scale_factor * self.GRAVITY_CONSTANT, 4)} "
            f"{self.SOLAR_MASS_UNITS}"
        )
        return planet_mass
