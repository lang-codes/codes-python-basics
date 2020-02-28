# HEAD
# Classes - __init_subclass__() method
# DESCRIPTION
# Describes usage of __init_subclass__ method
# RESOURCES
# 


class InitSubclass():
    def __init_subclass__(cls, default_name, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.default_name = default_name    


class SubClass(InitSubclass, default_name="Bruce"):
    def __init__(self, val):
        print("val from SubClass", val)


o = SubClass(10)


# # Variation
# # https://docs.python.org/3/reference/datamodel.html#implementing-descriptors
# class Philosopher:
#     def __init_subclass__(cls, default_name, **kwargs):
#         super().__init_subclass__(**kwargs)
#         cls.default_name = default_name

# class AustralianPhilosopher(Philosopher, default_name="Bruce"):
#     pass

# Sample codes
# https://gist.github.com/pjeby/75ca26f8d2a7a0c68e30

