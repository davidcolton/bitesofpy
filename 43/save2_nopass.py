def get_profile(name='julian', profession='programmer', *ignore):
    if ignore:
        raise TypeError
    return(f'{name} is a {profession}')