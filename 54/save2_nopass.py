INDENTS = 4
SPACES = ' ' * INDENTS

def print_hanging_indents(poem):
    formatted_string = '\n'
    first_line = True
    
    for line in poem.split('\n'):
        if len(line) == 0:
            first_line = True
        elif first_line:
            formatted_string += f'{line.strip()}\n'
            first_line = False
        else:
            formatted_string += f'{SPACES}{line.strip()}\n'
        
    return formatted_string + '\n'
    
    
shakespeare_unformatted = """
                          To be, or not to be, that is the question:
                          Whether 'tis nobler in the mind to suffer

                          The slings and arrows of outrageous fortune,
                          Or to take Arms against a Sea of troubles,
                          """
                          
print(print_hanging_indents(shakespeare_unformatted))