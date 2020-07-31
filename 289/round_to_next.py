def round_to_next(number: int, multiple: int):
    diff = number % multiple
    if diff == 0:
        return number
    if multiple > 0:
        return number + (multiple - diff)
    else:
        return number + (multiple + abs(diff))
