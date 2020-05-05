import inspect
from collections import namedtuple

Inspected_Class = namedtuple("Inspected_Class", "name type")


def get_classes(mod):
    """Return a list of all classes in module 'mod'"""
    result = []
    classes = [
        Inspected_Class(class_def[0], class_def[1])
        for class_def in inspect.getmembers(mod, predicate=inspect.isclass)
    ]
    for insp_cls in classes:
        if insp_cls.name[0].isupper():
            result.append(insp_cls.name)

    return result
