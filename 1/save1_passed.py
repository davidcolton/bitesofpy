def sum_numbers(numbers=None):
    '''
    Write a function that can sum up numbers:
    It should receive a list of n numbers.
    If no argument is provided, return sum of numbers 1..100.
    Look closely to the type of the function's default argument ...
    Have fun!'''
    
    # Handle the None scenario
    if numbers is None:
        numbers = range(1, 101)

    # Handle empty lists    
    elif not numbers:
        numbers = [0]

    # Return the sum of numbers
    return sum(numbers)