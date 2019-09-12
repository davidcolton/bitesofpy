def _validate_rgb_tuple(rgb):
    for value in rgb:
        if not isinstance(value, int):
            raise ValueError
        if not (0 <= value <= 255):
            raise ValueError
    return True


def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    if _validate_rgb_tuple(rgb):
        r, g, b = rgb
        return "#{:02x}{:02x}{:02x}".format(r, g, b).upper()

