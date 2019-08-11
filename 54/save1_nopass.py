INDENTS = 4
SPACES = ' ' * INDENTS

def print_hanging_indents(poem):
    formatted_string = '\n'
    first_line = True
    
    for line in poem.split('\n'):
        print(line)
        if len(line) == 0:
            first_line = True
        elif first_line:
            formatted_string += f'{line.strip()}\n'
            first_line = False
        else:
            formatted_string += f'{SPACES}{line.strip()}\n'
        
    return formatted_string + '\n'