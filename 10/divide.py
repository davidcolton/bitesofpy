def positive_divide(numerator, denominator):
    try:
        res = numerator / denominator
    except TypeError:
        raise TypeError
    except ZeroDivisionError:
        return 0
    else:
        if res < 0:
            raise ValueError
        else:
            return res


print(positive_divide(3, 0))

