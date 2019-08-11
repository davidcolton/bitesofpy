def get_profile(*ignore, name='julian', profession='programmer'):
    if ignore:
        raise TypeError
    return(f'{name} is a {profession}')