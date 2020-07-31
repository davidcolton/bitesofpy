from typing import List, TypeVar

T = TypeVar("T", int, float)


def n_digit_numbers(numbers: List[T], n: int) -> List[int]:
    new_numbers = []
    for number in numbers:
        sign = -1 if number < 0 else 1
        str_number = str(abs(number)).replace(".", "")
        if len(str_number) > n:
            new_number = int(str_number[:n])
        else:
            new_number = int(str_number.ljust(n, "0"))
        new_numbers.append(new_number * sign)
    return new_numbers

