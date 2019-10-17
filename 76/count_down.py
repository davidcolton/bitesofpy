from functools import singledispatch


def _print_string_countdown(str):
    for n in range(len(str), 0, -1):
        print(str[:n])


@singledispatch
def count_down(data_type):
    # TODO: Learn how to use singledispatch!
    raise ValueError


@count_down.register(int)
@count_down.register(float)
@count_down.register(str)
def _(data_type):
    _print_string_countdown(str(data_type))


@count_down.register(list)
@count_down.register(tuple)
@count_down.register(set)
@count_down.register(range)
def _(data_type):
    _print_string_countdown("".join(str(x) for x in data_type))


@count_down.register(dict)
def _(data_type):
    _print_string_countdown("".join(str(x) for x in data_type.keys()))
