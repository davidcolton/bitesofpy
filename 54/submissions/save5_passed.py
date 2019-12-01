INDENTS = 4
SPACES = ' ' * INDENTS

def print_hanging_indents(poem):
    formatted_string = ''
    first_line = True
    
    for line in poem.split('\n'):
        if len(line) == 0:
            first_line = True
        elif first_line:
            formatted_string += f'{line.strip()}\n'
            first_line = False
        else:
            formatted_string += f'{SPACES}{line.strip()}\n'
        
    print(formatted_string)