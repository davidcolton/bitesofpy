def divide_numbers(numerator, denominator):
    """For this exercise you can assume numerator and denominator are of type
       int/str/float.
       Try to convert numerator and denominator to int types, if that raises a
       ValueError reraise it. Following do the division and return the result.
       However if denominator is 0 catch the corresponding exception Python
       throws (cannot divide by 0), and return 0"""
    def to_int(num):
        try:
            return int(num)
        except ValueError:
            raise ValueError(f'Cannot convert {num} to int')
    
    numerator_int = to_int(numerator)
    denominator_int = to_int(denominator)

    try:
        return numerator_int / denominator_int
    except ZeroDivisionError:
        return 0        