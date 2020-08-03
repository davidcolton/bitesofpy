def is_armstrong(n: int) -> bool:
    return sum([int(num)**len(str(n)) for num in str(n)]) == n