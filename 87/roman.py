numbers = dict(
    [(1000, "M"), (500, "D"), (100, "C"), (50, "L"), (10, "X"), (5, "V"), (1, "I")]
)


def _helper(multiplyer, num):
    if num == 5 or num == 1:
        return numbers[num * multiplyer]
    elif num == 9:
        return numbers[1 * multiplyer] + numbers[1 * multiplyer * 10]
    elif num == 4:
        return numbers[1 * multiplyer] + numbers[5 * multiplyer]
    else:
        fives, units = divmod(num, 5)
        if fives:
            return numbers[5 * multiplyer] + numbers[1 * multiplyer] * units
        else:
            return numbers[1 * multiplyer] * units


def romanize(decimal_number):
    """Takes a decimal number int and converts its Roman Numeral str"""
    if not isinstance(decimal_number, int) or not (0 < decimal_number < 4000):
        raise ValueError
    # Type number to string, left fill with zero, split, then back to int
    # So 3999:
    #    thou = 3
    #    hun  = 9
    #    ten  = 9
    #    unit = 9
    roman = ""
    thou, hun, ten, unit = [int(n) for n in list(str(decimal_number).zfill(4))]
    if thou:
        roman += numbers[1000] * thou
    if hun:
        roman += _helper(100, hun)
    if ten:
        roman += _helper(10, ten)
    if unit:
        roman += _helper(1, unit)

    return roman


print(romanize(3500))
