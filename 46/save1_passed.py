def fizzbuzz(num):
    fizz = 3
    buzz = 5
    fizz_buzz = 15
    if num % fizz_buzz == 0:
        return 'Fizz Buzz'
    elif num % buzz == 0:
        return 'Buzz'
    elif num % fizz == 0:
        return 'Fizz'
    else:
        return num