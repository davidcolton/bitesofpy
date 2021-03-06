import operator


def get_operator_fn(op):
    return {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }[op]


def simple_calculator(calculation):
    """Receives 'calculation' and returns the calculated result,

       Examples - input -> output:
       '2 * 3' -> 6
       '2 + 6' -> 8

       Support +, -, * and /, use "true" division (so 2/3 is .66
       rather than 0)

       Make sure you convert both numbers to ints.
       If bad data is passed in, raise a ValueError.
       
       https://stackoverflow.com/questions/1740726/turn-string-into-operator
    """
    try:
        op1, op, op2 = calculation.split(" ")
        return get_operator_fn(op)(int(op1), int(op2))
    except:
        raise ValueError

