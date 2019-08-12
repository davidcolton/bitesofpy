def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    if not isinstance(value, (int, float)):
        raise TypeError
    if not isinstance(fmt, str):
        raise TypeError
    if not fmt.lower() in ['cm', 'in']:
        raise ValueError

    fmtl = fmt.lower()

    if fmtl == 'cm':
        return round(value * 2.54, 4)
    else:
        return round(value / 2.54, 4)

