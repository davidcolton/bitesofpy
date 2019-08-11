names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""
    # Zip the 2 lists together
    single_list = list(zip(names, countries))
    
    # Iterate over the single list using enumerate
    for position, list_item in enumerate(single_list):
        print(f'{position + 1}. {list_item[0] :<11} {list_item[1]}')

enumerate_names_countries()