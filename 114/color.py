import os
import sys
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
color_values_module = os.path.join("/tmp", "color_values.py")
urllib.request.urlretrieve("https://bit.ly/2MSuu4z", color_values_module)
sys.path.append("/tmp")

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        self.rgb = COLOR_NAMES.get(color.upper(), None)
        self.color = color.lower()

    @classmethod
    def hex2rgb(cls, hex):
        """Class method that converts a hex value into an rgb one"""
        h = hex.lstrip("#")
        return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))

    @classmethod
    def rgb2hex(cls, rgb):
        """Class method that converts an rgb value into a hex one"""
        if len(rgb) != 3:
            raise ValueError
        for cc in rgb:
            if cc < 0 or cc > 255:
                raise ValueError
        r, g, b = rgb
        return "#{:02x}{:02x}{:02x}".format(r, g, b)

    def __repr__(self):
        """Returns the repl of the object"""
        return f"Color('{self.color}')"

    def __str__(self):
        """Returns the string value of the color object"""
        return str(self.rgb)
