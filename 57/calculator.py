import argparse


def calculator(operation, numbers):
    """TODO 1:
       Create a calculator that takes an operation and list of numbers.
       Perform the operation returning the result rounded to 2 decimals"""
    if not numbers:
        raise SystemExit
    total = float(numbers[0])
    if operation == "[ADD ...]":
        for n in numbers[1:]:
            total += float(n)
    if operation == "[SUB ...]":
        for n in numbers[1:]:
            total -= float(n)
    if operation == "[MUL ...]":
        for n in numbers[1:]:
            total *= float(n)
    if operation == "[DIV ...]":
        for n in numbers[1:]:
            total /= float(n)

    return round(total, 2)


def create_parser():
    """TODO 2:
       Create an ArgumentParser object:
       - have one operation argument,
       - have one or more integers that can be operated on.
       Returns a argparse.ArgumentParser object.

       Note that type=float times out here so do the casting in the calculator
       function above!"""
    parser = argparse.ArgumentParser(
        prog="calculator.py", description="A simple calculator"
    )

    parser.add_argument(
        "-a", "--add", dest="[ADD ...]", help="Sums numbers", type=str, nargs="*"
    )
    parser.add_argument(
        "-s", "--sub", dest="[SUB ...]", help="Subtracts numbers", type=str, nargs="*"
    )
    parser.add_argument(
        "-m", "--mul", dest="[MUL ...]", help="Sums numbers", type=str, nargs="*"
    )
    parser.add_argument(
        "-d", "--div", dest="[DIV ...]", help="Divides numbers", type=str, nargs="*"
    )
    return parser


def call_calculator(args=None, stdout=False):
    """Provided/done:
       Calls calculator with provided args object.
       If args are not provided get them via create_parser,
       if stdout is True print the result"""
    parser = create_parser()

    if args is None:
        args = parser.parse_args()

    # taking the first operation in args namespace
    # if combo, e.g. -a and -s, take the first one
    for operation, numbers in vars(args).items():
        if numbers is None:
            continue

        try:
            res = calculator(operation, numbers)
        except ZeroDivisionError:
            res = 0

        if stdout:
            print(res)

        return res


if __name__ == "__main__":
    call_calculator(stdout=True)
