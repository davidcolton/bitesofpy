def dec_to_base(number, base):
    """
    Input: number is the number to be converted
           base is the new base  (eg. 2, 6, or 8)
    Output: the converted number in the new base without the prefix (eg. '0b')
    """
    # The Base or stopping case
    if number < base:
        return number
    # Recursion of the Floor division of the number by the base and the base
    #    Multiple by 10 to shift left
    #    i.e. 1's to 10's to 100's etc.
    # Plus the modulus
    else:
        return (dec_to_base(number // base, base) * 10) + (number % base)
