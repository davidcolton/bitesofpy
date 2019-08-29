# see __mro__ output in Bite description


class Person(object):
    def __str__(self):
        return "I am a person"


class Father(Person):
    def __str__(self):
        prefix = super().__str__()
        return prefix + " and cool daddy"


class Mother(Person):
    def __str__(self):
        prefix = super().__str__()
        return prefix + " and awesome mom"


class Child(Father, Mother):
    def __str__(self):
        return "I am the coolest kid"
