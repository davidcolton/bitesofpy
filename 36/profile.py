def get_profile(name=None, age=None, *args, **kwargs):
    profile = dict()
    if not name or not age:
        raise TypeError
    if not isinstance(age, int) or len(args) > 5:
        raise ValueError
    profile["name"] = name
    profile["age"] = age
    if args:
        profile["sports"] = sorted([s for s in args])
    if kwargs:
        profile["awards"] = kwargs
    return profile

