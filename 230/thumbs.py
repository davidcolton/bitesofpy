THUMBS_UP, THUMBS_DOWN = "👍", "👎"


class Thumbs(int):
    def __mul__(self, multiplier):
        if multiplier == 0:
            raise ValueError("Specify a number")
        if multiplier < 4 and multiplier > 0:
            return THUMBS_UP * multiplier
        elif multiplier >= 4:
            return f"{THUMBS_UP} ({multiplier}x)"
        elif multiplier < 0 and multiplier > -4:
            return THUMBS_DOWN * abs(multiplier)
        elif multiplier <= -4:
            return f"{THUMBS_DOWN} ({abs(multiplier)}x)"

    def __rmul__(self, multiplier):
        if multiplier == 0:
            raise ValueError("Specify a number")
        if multiplier < 4 and multiplier > 0:
            return THUMBS_UP * multiplier
        elif multiplier >= 4:
            return f"{THUMBS_UP} ({multiplier}x)"
        elif multiplier < 0 and multiplier > -4:
            return THUMBS_DOWN * abs(multiplier)
        elif multiplier <= -4:
            return f"{THUMBS_DOWN} ({abs(multiplier)}x)"

